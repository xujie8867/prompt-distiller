#!/usr/bin/env python3
"""Prompt Distiller - 10-point audit scoring for image generation prompts."""
import re, json, sys

CHECKS = {
    "camera_brand": {
        "weight": 10,
        "pattern": r'(sony\s+A\d|canon\s+(EOS\s+)?R\d|nikon\s+Z\d|hasselblad\s+H\d|leica\s+(M\d|SL)|fujifilm\s+GFX|phase\s+one\s+XF|pentax\s+K)',
        "scoring": "match=10, no_match=0",
        "human": "相机品牌型号"
    },
    "lens_aperture": {
        "weight": 15,
        "pattern": r'\d{2,3}mm\s+f/?\d',
        "scoring": "match=10, no_match=0",
        "human": "镜头焦距+光圈"
    },
    "lighting_scheme": {
        "weight": 15,
        "pattern": r'(rembrandt\s+light|butterfly\s+light|split\s+light|loop\s+light|rim\s+light|golden\s+hour\s+(side|back|light)|window\s+light|softbox|chiaroscuro|key\s+light|fill\s+light)',
        "scoring": "match=10, partial=8 for golden_hour+vague=4 for light, no_match=0",
        "human": "具体布光方案"
    },
    "skin_realism": {
        "weight": 15,
        "pattern": r'(pores|micro[\s-]?texture|peach\s+fuzz|NOT\s*(flawless|airbrush|plastic|smooth))',
        "scoring": "match=10, no_match=0 (only for portrait/people prompts)",
        "human": "真实皮肤描述"
    },
    "negative": {
        "weight": 10,
        "pattern": r'(blurry|motion\s*blur|soft\s*focus|plastic\s*skin|airbrush|flawless\s*skin|oversmoothed|waxy\s*skin|low\s*quality|AI\s*artifact)',
        "scoring": "0-2 matches=3, 3-4 matches=7, 5+=10",
        "human": "负向词"
    },
    "sharpness": {
        "weight": 10,
        "pattern": r'(tack[\s-]?sharp|razor[\s-]?sharp|crisp\s*focus|micro[\s-]?contrast|maximum\s*sharpness)',
        "scoring": "match=10, no_match=0",
        "human": "锐度关键词"
    },
    "authority": {
        "weight": 5,
        "pattern": r'(national\s*geographic|vogue|annie\s*leibovitz|steve\s*mccurry|peter\s*lindbergh|mario\s*testino|condé\s*nast)',
        "scoring": "match=10, no_match=0",
        "human": "权威摄影锚点"
    },
    "composition": {
        "weight": 5,
        "pattern": r'(shallow\s*depth|bokeh|catchlight|rule\s*of\s*thirds|leading\s*lines|creamy\s*background)',
        "scoring": "match=10, no_match=0",
        "human": "构图描述"
    },
    "resolution": {
        "weight": 5,
        "pattern": r'(8K|32K|hyper[\s-]?detailed|raw\s*photo|film\s*grain|high[\s-]?res)',
        "scoring": "match=10, no_match=0",
        "human": "分辨率标注"
    },
    "portrait_ethnic": {
        "weight": 10,
        "pattern": r'(african|asian|indian|latina|middle\s*eastern|ebony\s*skin|olive\s*skin|melanin|ethnic|maasai|indigenous|east\s*asian|south\s*asian)',
        "scoring": "match=10, vague=5, no_match=0 (only for portrait/people prompts)",
        "human": "人种肤色精确度"
    }
}

def is_portrait(prompt):
    """Check if prompt is a portrait/people prompt."""
    people_words = ['portrait', 'person', 'woman', 'man', 'people', 'face', 'skin', 'model', 'elder', 'baby', 'girl', 'boy', 'actor', 'figure', 'fashion', 'editorial', 'beauty']
    prompt_lower = prompt.lower()
    return any(w in prompt_lower for w in people_words)

def audit(prompt):
    """Score a prompt against 10 quality checks."""
    scores = {}
    total_weight = 0
    weighted_score = 0
    
    for check_name, check in CHECKS.items():
        # Skip portrait_ethnic and skin_realism for non-portrait prompts
        if check_name in ('portrait_ethnic', 'skin_realism') and not is_portrait(prompt):
            scores[check_name] = {"score": "N/A (非人像)", "weight": 0}
            continue
        
        matches = len(re.findall(check['pattern'], prompt, re.IGNORECASE))
        
        if check_name == 'negative':
            if matches >= 5: score = 10
            elif matches >= 3: score = 7
            elif matches >= 1: score = 3
            else: score = 0
        elif check_name == 'lighting_scheme':
            if matches > 0: score = 10
            elif re.search(r'golden\s*hour', prompt, re.IGNORECASE): score = 8
            elif re.search(r'(lighting|lit\s)', prompt, re.IGNORECASE): score = 4
            else: score = 0
        elif check_name == 'portrait_ethnic':
            if matches > 0: score = 10
            elif re.search(r'(woman|man|person|people)', prompt, re.IGNORECASE): score = 0
            else: score = 0
        else:
            score = 10 if matches > 0 else 0
        
        weight = check['weight']
        scores[check_name] = {"score": score, "weight": weight, "matches": matches}
        weighted_score += score * weight / 100
        total_weight += weight
    
    # Normalize to 0-100
    if total_weight > 0:
        final_score = weighted_score * 100 / total_weight
    else:
        final_score = 0
    
    return {
        "total_score": round(final_score, 1),
        "level": "🏆 大师级" if final_score >= 90 else "👍 良好" if final_score >= 70 else "⚠️ 需优化" if final_score >= 40 else "❌ 低质量",
        "checks": {k: v for k, v in scores.items()}
    }

if __name__ == '__main__':
    prompt = sys.stdin.read().strip() if not sys.argv[1:] else sys.argv[1]
    result = audit(prompt)
    print(json.dumps(result, indent=2, ensure_ascii=False))
