import matplotlib.pyplot as plt
import numpy as np
import platform
from matplotlib import font_manager, rc

# 한글 폰트 설정
if platform.system() == 'Windows':
    font_name = 'Malgun Gothic'
elif platform.system() == 'Darwin':
    font_name = 'AppleGothic'
else:
    font_name = 'DejaVu Sans'
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

models = [
    'claude-4-sonnet', 'claude-3.5-sonnet', 'o3', 'gemini-2.5-pro', 'gemini-2.5-flash',
    'gpt-4.1', 'claude-4-opus', 'claude-4-opus (MAX)', 'gemini-2.5-pro-preview-06-05',
    'claude-3.7-sonnet', 'cursor-small', 'claude-3.5-haiku', 'gpt-4o', 'o4-mini',
    'deepseek-r1-0528', 'deepseek-v3.1', 'grok-3-beta', 'grok-3-mini', 'o3-pro'
]
scores = {
    '코딩':      [9, 8, 9, 8, 7, 9, 10, 10, 8, 8, 3, 7, 9, 7, 7, 8, 7, 5, 10],
    '수리':      [9, 7, 8, 7, 6, 8, 9, 9, 7, 7, 3, 6, 9, 6, 7, 8, 6, 5, 9],
    '추론':      [9, 8, 9, 8, 7, 9, 10, 10, 8, 8, 3, 7, 9, 7, 7, 8, 7, 5, 10],
    '멀티모달':  [7, 6, 7, 9, 8, 8, 8, 8, 9, 6, 2, 5, 10, 7, 5, 6, 8, 7, 8],
    '속도/비용': [7, 8, 6, 7, 9, 7, 5, 5, 7, 8, 10, 9, 8, 9, 8, 8, 7, 9, 5]
}

for cat, vals in scores.items():
    # 내림차순 정렬
    sorted_indices = np.argsort(vals)[::-1]
    sorted_vals = [vals[i] for i in sorted_indices]
    sorted_models = [models[i] for i in sorted_indices]
    fig, ax = plt.subplots(figsize=(16,8))
    ax.bar(range(len(models)), sorted_vals, color='skyblue')
    ax.set_ylabel('점수(0~10)')
    ax.set_title(f'LLM 모델별 {cat} 점수 (내림차순)')
    ax.set_xticks(range(len(models)))
    ax.set_xticklabels(sorted_models, rotation=30, ha='right')
    ax.set_ylim(0, 10)
    plt.tight_layout()
    safe_cat = cat.replace('/', '_')
    plt.savefig(f'llm_barchart_{safe_cat}.png')
    plt.close() 