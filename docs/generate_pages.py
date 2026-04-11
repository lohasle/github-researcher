#!/usr/bin/env python3
"""
GitHub Pages HTML Generator
Reads Markdown files with YAML frontmatter and generates static HTML pages.
"""

import os
import re
import glob
import yaml
import markdown
from datetime import datetime

# === Paths ===
BASE_DIR = '/home/lohasle/.openclaw/workspace-github-researcher'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DAILY_DIR = os.path.join(BASE_DIR, 'daily')
PROJECTS_DIR = os.path.join(BASE_DIR, 'projects')
INDEXES_DIR = os.path.join(BASE_DIR, 'indexes')

# === CSS (extracted from index.html design) ===
CSS = '''    <style>
        :root {
            --primary: #7C3AED;
            --primary-light: #A78BFA;
            --primary-dark: #5B21B6;
            --cta: #06B6D4;
            --cta-light: #67E8F9;
            --bg: #FAF5FF;
            --bg-card: #FFFFFF;
            --text: #1E1B4B;
            --text-muted: #6B7280;
            --border: #E9D5FF;
            --success: #10B981;
            --warning: #F59E0B;
            --shadow: 0 4px 6px -1px rgba(124, 58, 237, 0.1), 0 2px 4px -2px rgba(124, 58, 237, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(124, 58, 237, 0.12), 0 4px 6px -4px rgba(124, 58, 237, 0.1);
            --radius: 12px;
            --radius-sm: 8px;
        }
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        html { scroll-behavior: smooth; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.7;
            min-height: 100vh;
        }
        .nav {
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 100;
            padding: 0 24px;
        }
        .nav-inner {
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 64px;
        }
        .nav-brand {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 700;
            font-size: 18px;
            color: var(--primary);
            text-decoration: none;
        }
        .nav-brand svg { width: 28px; height: 28px; }
        .nav-links {
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .nav-links a {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            color: var(--text-muted);
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s;
        }
        .nav-links a:hover { background: var(--primary); color: white; }
        .nav-links a svg { width: 16px; height: 16px; }
        .nav-links a.active { background: var(--primary); color: white; }
        .container { max-width: 1100px; margin: 0 auto; padding: 40px 24px 60px; }
        .hero { text-align: center; padding: 60px 0 50px; }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            color: white;
            padding: 6px 16px;
            border-radius: 100px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 24px;
            letter-spacing: 0.5px;
        }
        .hero-badge .dot { width: 6px; height: 6px; background: var(--cta-light); border-radius: 50%; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.6; transform: scale(0.8); } }
        .hero h1 { font-size: 42px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 16px; letter-spacing: -1px; }
        .hero p { font-size: 17px; color: var(--text-muted); max-width: 560px; margin: 0 auto 36px; }
        .hero-actions { display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap; }
        .btn-primary { display: inline-flex; align-items: center; gap: 8px; background: var(--primary); color: white; padding: 12px 24px; border-radius: var(--radius-sm); text-decoration: none; font-weight: 600; font-size: 15px; transition: all 0.2s; border: none; cursor: pointer; box-shadow: var(--shadow); }
        .btn-primary:hover { background: var(--primary-dark); transform: translateY(-1px); box-shadow: var(--shadow-lg); }
        .btn-secondary { display: inline-flex; align-items: center; gap: 8px; background: white; color: var(--primary); padding: 12px 24px; border-radius: var(--radius-sm); text-decoration: none; font-weight: 600; font-size: 15px; transition: all 0.2s; border: 2px solid var(--border); }
        .btn-secondary:hover { border-color: var(--primary); background: var(--bg); }
        .stats-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 48px; }
        .stat-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px 20px; text-align: center; transition: all 0.2s; box-shadow: var(--shadow); }
        .stat-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); border-color: var(--primary-light); }
        .stat-icon { width: 44px; height: 44px; background: linear-gradient(135deg, var(--primary), var(--primary-light)); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px; font-size: 20px; }
        .stat-number { font-size: 28px; font-weight: 800; color: var(--primary); margin-bottom: 4px; }
        .stat-label { font-size: 13px; color: var(--text-muted); font-weight: 500; }
        .section-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }
        .section-title { display: flex; align-items: center; gap: 10px; font-size: 20px; font-weight: 700; color: var(--text); }
        .section-title .icon { width: 36px; height: 36px; background: linear-gradient(135deg, var(--primary), var(--cta)); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 18px; }
        .section-link { font-size: 13px; color: var(--primary); text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 4px; }
        .section-link:hover { text-decoration: underline; }
        .card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; margin-bottom: 48px; }
        .card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; transition: all 0.2s; box-shadow: var(--shadow); text-decoration: none; color: inherit; display: block; }
        .card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); border-color: var(--primary-light); }
        .card-top { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 14px; }
        .card-emoji { font-size: 32px; line-height: 1; }
        .card-stars { background: linear-gradient(135deg, var(--primary), var(--primary-light)); color: white; padding: 4px 10px; border-radius: 100px; font-size: 12px; font-weight: 700; }
        .card-title { font-size: 16px; font-weight: 700; margin-bottom: 8px; color: var(--text); }
        .card-desc { font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px; }
        .card-tags { display: flex; flex-wrap: wrap; gap: 6px; }
        .tag { padding: 3px 10px; border-radius: 100px; font-size: 11px; font-weight: 600; border: 1px solid; }
        .tag-purple { background: #F3E8FF; color: var(--primary); border-color: var(--border); }
        .tag-cyan { background: #ECFEFF; color: #0891B2; border-color: #A5F3FC; }
        .tag-green { background: #ECFDF5; color: #059669; border-color: #A7F3D0; }
        .tag-orange { background: #FFF7ED; color: #C2410C; border-color: #FED7AA; }
        .trend-list { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; margin-bottom: 48px; box-shadow: var(--shadow); }
        .trend-item { display: flex; align-items: center; padding: 16px 20px; border-bottom: 1px solid var(--border); gap: 16px; transition: background 0.15s; }
        .trend-item:last-child { border-bottom: none; }
        .trend-item:hover { background: var(--bg); }
        .trend-rank { width: 28px; height: 28px; border-radius: 6px; background: var(--primary); color: white; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
        .trend-rank.top { background: linear-gradient(135deg, #F59E0B, #EF4444); }
        .trend-content { flex: 1; min-width: 0; }
        .trend-title { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 2px; }
        .trend-meta { font-size: 12px; color: var(--text-muted); }
        .trend-score { padding: 4px 12px; border-radius: 100px; font-size: 12px; font-weight: 700; background: #F3E8FF; color: var(--primary); border: 1px solid var(--border); flex-shrink: 0; }
        .trend-score.high { background: #ECFDF5; color: #059669; border-color: #A7F3D0; }
        .brief-card { background: linear-gradient(135deg, var(--primary-dark), var(--primary)); border-radius: var(--radius); padding: 36px 40px; color: white; margin-bottom: 48px; position: relative; overflow: hidden; box-shadow: var(--shadow-lg); }
        .brief-card::before { content: ''; position: absolute; top: -60px; right: -60px; width: 200px; height: 200px; background: rgba(255,255,255,0.08); border-radius: 50%; }
        .brief-card::after { content: ''; position: absolute; bottom: -40px; left: 40px; width: 120px; height: 120px; background: rgba(255,255,255,0.05); border-radius: 50%; }
        .brief-date { font-size: 13px; opacity: 0.75; margin-bottom: 8px; font-weight: 500; }
        .brief-title { font-size: 24px; font-weight: 800; margin-bottom: 16px; }
        .brief-text { font-size: 15px; opacity: 0.9; line-height: 1.7; max-width: 700px; margin-bottom: 24px; }
        .brief-cta { display: inline-flex; align-items: center; gap: 8px; background: white; color: var(--primary); padding: 10px 20px; border-radius: var(--radius-sm); text-decoration: none; font-weight: 700; font-size: 14px; transition: all 0.2s; position: relative; z-index: 1; }
        .brief-cta:hover { transform: translateY(-1px); }
        .category-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 48px; }
        .category-pill { display: flex; align-items: center; gap: 6px; padding: 8px 16px; background: white; border: 1px solid var(--border); border-radius: 100px; font-size: 13px; font-weight: 500; color: var(--text); text-decoration: none; transition: all 0.2s; box-shadow: var(--shadow); }
        .category-pill:hover { background: var(--primary); color: white; border-color: var(--primary); }
        .category-pill .emoji { font-size: 15px; }
        .footer { text-align: center; padding: 32px 0; border-top: 1px solid var(--border); color: var(--text-muted); font-size: 13px; }
        .footer a { color: var(--primary); text-decoration: none; }
        .footer a:hover { text-decoration: underline; }
        @media (max-width: 768px) { .hero h1 { font-size: 30px; } .stats-row { grid-template-columns: repeat(2, 1fr); } .nav-links span { display: none; } .brief-card { padding: 28px 24px; } }
        @media (max-width: 480px) { .card-grid { grid-template-columns: 1fr; } }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .hero, .stats-row, .brief-card, .card-grid, .trend-list { animation: fadeInUp 0.5s ease-out; }
        .stats-row { animation-delay: 0.1s; animation-fill-mode: both; }
        .brief-card { animation-delay: 0.15s; animation-fill-mode: both; }
        .card-grid { animation-delay: 0.2s; animation-fill-mode: both; }
        .trend-list { animation-delay: 0.25s; animation-fill-mode: both; }
    </style>'''

NAV = '''    <nav class="nav">
        <div class="nav-inner">
            <a href="/github-researcher/index.html" class="nav-brand">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>
                GitHub 趋势研究
            </a>
            <div class="nav-links">
                <a href="/github-researcher/index.html" id="nav-home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><span>首页</span></a>
                <a href="/github-researcher/daily.html" id="nav-daily"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg><span>日报</span></a>
                <a href="/github-researcher/projects.html" id="nav-projects"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg><span>项目</span></a>
                <a href="/github-researcher/trends.html" id="nav-trends"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg><span>趋势</span></a>
            </div>
        </div>
    </nav>'''

FOOTER = '''    <footer class="footer">
        <p>由 <strong>GitHub Researcher Agent</strong> 自动生成 · <a href="https://github.com/lohasle/github-researcher">GitHub 仓库</a> · <a href="https://lohasle.github.io/github-researcher/">在线浏览</a></p>
        <p style="margin-top:8px; opacity:0.7;">持续跟踪 · 每日更新 · 架构视角</p>
    </footer>'''


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        fm = {}

    return fm, parts[2]


def get_fm(fm, key, default):
    """Safely get value from frontmatter with default."""
    val = fm.get(key, default)
    return val if val is not None else default


def tag_class(tag):
    """Return CSS class for tag."""
    tag_lower = tag.lower()
    if '基础设施' in tag or 'poc' in tag_lower: return 'tag-green'
    if 'mcp' in tag_lower: return 'tag-cyan'
    if '平台' in tag: return 'tag-cyan'
    if '泡沫' in tag: return 'tag-orange'
    return 'tag-purple'


# === Generate index.html ===
def generate_index():
    # Read latest daily
    daily_files = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True)

    latest_daily_fm = {}
    latest_daily_content = ''
    if daily_files:
        with open(daily_files[0], 'r') as f:
            content = f.read()
        latest_daily_fm, latest_daily_content = parse_frontmatter(content)

    # Read all projects for key_projects
    project_files = sorted(glob.glob(os.path.join(PROJECTS_DIR, '*.md')))
    all_projects = []
    for pf in project_files:
        with open(pf, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        if fm:
            fm['href'] = fm.get('href', f"projects/{os.path.basename(pf).replace('.md', '.html')}")
            all_projects.append(fm)

    # Use frontmatter data or provide defaults
    title = get_fm(latest_daily_fm, 'title', 'GitHub 趋势研究')
    summary = get_fm(latest_daily_fm, 'summary', '持续跟踪 GitHub 热门项目与开源趋势')
    hero_badge = get_fm(latest_daily_fm, 'hero_badge', '持续更新中')
    date_str = get_fm(latest_daily_fm, 'date', datetime.now().strftime('%Y-%m-%d'))

    # === Dynamic stats: always compute from actual data ===
    # Use aggregate_all_projects() for consistency with projects page
    aggregated = aggregate_all_projects()
    real_project_count = len(aggregated)

    # Count daily reports (daily/*.md)
    daily_files_for_stats = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')))
    real_daily_count = len(daily_files_for_stats)

    # Count unique trend directions across all dailies
    unique_directions = set()
    for df in daily_files_for_stats:
        with open(df, 'r') as fp:
            c = fp.read()
        fm_d, _ = parse_frontmatter(c)
        for t in (fm_d.get('trends') or []):
            if t.get('name'):
                unique_directions.add(t['name'])
    real_directions_count = len(unique_directions)

    # Sum weekly stars from latest daily's weekly_stars field (keep as-is if string)
    weekly_stars = get_fm(latest_daily_fm, 'stats', {}).get('weekly_stars', 'N/A')

    # Override stats with real computed values (ignores frontmatter project_count)
    stats = {
        'project_count': real_project_count,
        'daily_updates': real_daily_count,
        'core_directions': real_directions_count,
        'weekly_stars': weekly_stars
    }

    trends = get_fm(latest_daily_fm, 'trends', [
        {'rank': 1, 'name': 'Multi-Agent Orchestration', 'projects': ['hermes-agent'], 'score': 60},
        {'rank': 2, 'name': 'MCP 协议扩散', 'projects': ['GitNexus', 'qmd'], 'score': 58},
    ])

    key_projects = get_fm(latest_daily_fm, 'key_projects', all_projects[:3])

    # Stats HTML
    stats_html = f'''
            <div class="stat-card">
                <div class="stat-icon">📊</div>
                <div class="stat-number">{stats['project_count']}</div>
                <div class="stat-label">深度分析项目</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🔥</div>
                <div class="stat-number">{stats['daily_updates']}</div>
                <div class="stat-label">日更日报</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🎯</div>
                <div class="stat-number">{stats['core_directions']}</div>
                <div class="stat-label">核心跟踪方向</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">⭐</div>
                <div class="stat-number">{stats['weekly_stars']}</div>
                <div class="stat-label">本周总 Star 增速</div>
            </div>'''

    # Brief card
    brief_date = f"📅 {date_str} · 今日核心判断"
    brief_title = summary
    # Dynamic brief_text from latest daily
    trends_latest = get_fm(latest_daily_fm, 'trends', [])
    top_trend = trends_latest[0]['name'] if trends_latest else summary
    brief_text = summary + (f" 今日头条趋势:{top_trend}。" if trends_latest else "")

    daily_date_filename = f"daily/{os.path.basename(daily_files[0]).replace('.md', '.html')}" if daily_files else 'daily/2026-04-07.html'

    # Key projects cards
    project_cards = ''
    for p in key_projects[:3]:
        name = p.get('title', p.get('name', 'Unknown'))
        emoji = p.get('emoji', '📦')
        stars = p.get('stars', p.get('stars_per_day', 'N/A'))
        if isinstance(stars, int):
            stars = f"{stars:,} stars/day"
        desc = p.get('desc', p.get('summary', ''))
        category = p.get('category', '')
        tags = p.get('tags', [category]) if isinstance(p.get('tags'), list) else [category]
        score = p.get('score', 'N/A')
        href = p.get('href', f"projects/{make_slug(name)}.html")
        tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags[:3]])
        project_cards += f'''
                <a href="/github-researcher/{href}" class="card">
                    <div class="card-top">
                        <div class="card-emoji">{emoji}</div>
                        <div class="card-stars">{stars}</div>
                    </div>
                    <div class="card-title">{name}</div>
                    <div class="card-desc">{desc}</div>
                    <div class="card-tags">{tag_html}</div>
                </a>'''

    # Trend list
    trend_rows = ''
    for t in trends[:4]:
        rank = t.get('rank', 0)
        name = t.get('name', 'Unknown')
        projects = t.get('projects', [])
        score_val = t.get('score', 0)
        is_high = score_val >= 55 if isinstance(score_val, int) else False
        rank_class = 'top' if rank <= 2 else ''
        score_class = 'high' if is_high else ''
        projects_str = ' · '.join(str(p) for p in projects[:3])
        trend_rows += f'''
                <div class="trend-item">
                    <div class="trend-rank {rank_class}">{rank}</div>
                    <div class="trend-content">
                        <div class="trend-title">{name}</div>
                        <div class="trend-meta">{projects_str}</div>
                    </div>
                    <div class="trend-score {score_class}">{score_val}/80</div>
                </div>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GitHub Researcher</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📊</text></svg>">
    <meta name="description" content="{summary}">
{CSS}
</head>
<body>
{NAV}
<main class="container">
        <section class="hero">
            <div class="hero-badge">
                <span class="dot"></span>
                {hero_badge}
            </div>
            <h1>GitHub 趋势研究</h1>
            <p>{summary}</p>
            <div class="hero-actions">
                <a href="/github-researcher/{daily_date_filename}" class="btn-primary">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                    今日简报
                </a>
                <a href="/github-researcher/projects.html" class="btn-secondary">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="14" y="0" width="7" height="7"/><rect x="0" y="14" width="7" height="7"/></svg>
                    重点项目
                </a>
            </div>
        </section>
        <section class="stats-row">{stats_html}
        </section>
        <section class="brief-card">
            <div class="brief-date">{brief_date}</div>
            <h2 class="brief-title">{brief_title}</h2>
            <p class="brief-text">{brief_text}</p>
            <a href="/github-researcher/{daily_date_filename}" class="brief-cta">阅读完整简报 →</a>
        </section>
        <section>
            <div class="section-header">
                <div class="section-title">
                    <div class="icon">⭐</div>
                    重点跟踪项目
                </div>
                <a href="/github-researcher/projects.html" class="section-link">查看全部 →</a>
            </div>
            <div class="card-grid">{project_cards}
            </div>
        </section>
        <section>
            <div class="section-header">
                <div class="section-title">
                    <div class="icon">📈</div>
                    趋势热榜
                </div>
                <a href="/github-researcher/trends.html" class="section-link">完整趋势表 →</a>
            </div>
            <div class="trend-list">{trend_rows}
            </div>
        </section>
        <section>
            <div class="section-header">
                <div class="section-title">
                    <div class="icon">🏷️</div>
                    核心关注领域
                </div>
            </div>
            <div class="category-row">
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">🤖</span> AI Agent / Multi-Agent</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">⚡</span> LLM Infra / MCP / AI Runtime</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">🛠️</span> 开发工具链 / IDE / Copilot</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">🌐</span> 前端框架 / Serverless / Edge</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">☸️</span> 云原生 / K8s / Service Mesh</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">🔄</span> 自动化 / Browser Use / RPA+AI</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">💾</span> 数据基础设施 / RAG / 向量 DB</a>
                <a href="/github-researcher/projects.html" class="category-pill"><span class="emoji">🔌</span> 基础设施标准 / 平台潜力</a>
            </div>
        </section>
</main>
{FOOTER}
</body>
</html>'''

    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(os.path.join(DOCS_DIR, 'index.html'), 'w') as f:
        f.write(html)
    print(f"Generated index.html")


# === Generate daily listing ===
def generate_daily_list():
    daily_files = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True)

    rows = ''
    for f in daily_files:
        date = os.path.basename(f).replace('.md', '')
        with open(f, 'r') as fp:
            content = fp.read()
        fm, _ = parse_frontmatter(content)
        title = fm.get('title', f'{date} 日报')
        summary = fm.get('summary', '')
        # Extract first line of summary
        topic = summary.split('。')[0] if summary else date

        rows += f'''        <tr>
            <td style="font-weight:600;">{date}</td>
            <td>{topic}</td>
            <td><a href="/github-researcher/daily/{date}.html" style="color:var(--primary);text-decoration:none;font-weight:500;">查看 →</a></td>
        </tr>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>日报索引 | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📊</text></svg>">
{CSS}
    <style>
        .page-header {{ padding: 48px 0 36px; text-align: center; }}
        .page-header h1 {{ font-size: 36px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 12px; }}
        .page-header p {{ color: var(--text-muted); font-size: 16px; }}
        .daily-table {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); margin-bottom: 48px; }}
        .daily-table table {{ width: 100%; border-collapse: collapse; }}
        .daily-table th {{ background: linear-gradient(135deg, var(--primary-dark), var(--primary)); color: white; padding: 14px 20px; text-align: left; font-size: 13px; font-weight: 600; letter-spacing: 0.5px; }}
        .daily-table td {{ padding: 16px 20px; border-bottom: 1px solid var(--border); font-size: 14px; }}
        .daily-table tr:last-child td {{ border-bottom: none; }}
        .daily-table tr:hover td {{ background: var(--bg); }}
    </style>
</head>
<body>
{NAV.replace('id="nav-daily"', 'id="nav-daily" class="active"')}
<script>document.getElementById('nav-daily').classList.add('active');</script>
<main class="container">
    <div class="page-header">
        <h1>📅 日报索引</h1>
        <p>每日 GitHub 趋势研究简报,持续跟踪不间断</p>
    </div>
    <div class="daily-table">
        <table>
            <thead>
                <tr>
                    <th>日期</th>
                    <th>核心主题</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
{rows}
            </tbody>
        </table>
    </div>
</main>
{FOOTER}
</body>
</html>'''

    with open(os.path.join(DOCS_DIR, 'daily.html'), 'w') as f:
        f.write(html)
    print(f"Generated daily.html with {len(daily_files)} entries")


# === Generate individual daily page ===
def generate_daily_page(filepath):
    date = os.path.basename(filepath).replace('.md', '')

    with open(filepath, 'r') as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    html_body = markdown.markdown(body, extensions=['tables', 'toc'])

    title = fm.get('title', f'{date} 日报')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📅</text></svg>">
{CSS}
    <style>
        .daily-content {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 40px 48px; box-shadow: var(--shadow); margin-bottom: 48px; max-width: 860px; margin-left: auto; margin-right: auto; }}
        .daily-content h1 {{ font-size: 28px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 8px; }}
        .daily-content h2 {{ font-size: 20px; font-weight: 700; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 12px; margin: 28px 0 14px; }}
        .daily-content h3 {{ font-size: 16px; font-weight: 700; color: var(--text); margin: 20px 0 10px; }}
        .daily-content table {{ border-collapse: collapse; width: 100%; margin: 14px 0; }}
        .daily-content th, .daily-content td {{ border: 1px solid var(--border); padding: 8px 12px; text-align: left; font-size: 13px; }}
        .daily-content th {{ background: var(--primary); color: white; font-weight: 600; }}
        .daily-content tr:nth-child(even) td {{ background: var(--bg); }}
        .daily-content blockquote {{ background: linear-gradient(135deg, #F3E8FF, #ECFEFF); border-left: 4px solid var(--primary); padding: 14px 18px; margin: 14px 0; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }}
        .daily-content ul, .daily-content ol {{ padding-left: 22px; margin: 10px 0; }}
        .daily-content li {{ margin: 6px 0; font-size: 14px; }}
        .daily-content p {{ font-size: 14px; margin-bottom: 12px; line-height: 1.7; }}
        .daily-content strong {{ color: var(--primary-dark); }}
        .back-link {{ display: inline-flex; align-items: center; gap: 6px; color: var(--primary); text-decoration: none; font-size: 14px; font-weight: 500; margin-bottom: 24px; }}
        .back-link:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
{NAV.replace('id="nav-daily"', 'id="nav-daily" class="active"')}
<main class="container">
    <a href="/github-researcher/daily.html" class="back-link">← 返回日报索引</a>
    <div class="daily-content">
        {html_body}
    </div>
</main>
{FOOTER}
</body>
</html>'''

    daily_html_dir = os.path.join(DOCS_DIR, 'daily')
    os.makedirs(daily_html_dir, exist_ok=True)
    with open(os.path.join(daily_html_dir, f'{date}.html'), 'w') as f:
        f.write(html)
    print(f"Generated daily/{date}.html")


# === Aggregate all projects from daily + projects dir ===
def aggregate_all_projects():
    """Merge projects from daily key_projects + projects/*.md, dedup by name."""
    merged = {}  # name -> project dict
    merged_by_slug = {}  # slug -> project dict

    # 1. Read projects/*.md for detailed profiles
    for pf in sorted(glob.glob(os.path.join(PROJECTS_DIR, '*.md'))):
        with open(pf, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        if not fm:
            continue
        key = fm.get('name', fm.get('title', os.path.basename(pf).replace('.md', '')))
        fm['_has_profile'] = True
        fm['_profile_slug'] = make_slug(key)
        merged[key] = fm
        # Also register by slug for cross-matching
        merged_by_slug[fm['_profile_slug']] = fm

    # 2. Walk daily/*.md newest-first, merge key_projects
    for df in sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True):
        date_str = os.path.basename(df).replace('.md', '')
        with open(df, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        kp_list = fm.get('key_projects', []) or []
        for p in kp_list:
            key = p.get('name', '')
            if not key:
                continue
            daily_slug = make_slug(key)
            # Try to match with existing profile by name or slug
            matched = merged.get(key) or merged_by_slug.get(daily_slug)
            if matched:
                for k, v in p.items():
                    if v is not None and k not in ('_has_profile', '_profile_slug'):
                        matched[k] = v
                matched['last_seen_date'] = date_str
                # Ensure the daily key also points to the same profile
                merged[key] = matched
            else:
                p = dict(p)
                p['last_seen_date'] = date_str
                merged[key] = p
            if 'first_seen_date' not in merged[key]:
                merged[key]['first_seen_date'] = date_str

    # Dedup: merged dict may contain same object under different keys
    seen = set()
    result = []
    for p in merged.values():
        pid = id(p)
        if pid not in seen:
            seen.add(pid)
            result.append(p)
    return result


# === Generate projects listing ===
def generate_projects_list():
    all_projects = aggregate_all_projects()
    # Sort by last_seen_date desc
    all_projects.sort(key=lambda p: p.get('last_seen_date', ''), reverse=True)

    cards = ''
    for p in all_projects:
        name = p.get('title', p.get('name', 'Unknown'))
        emoji = p.get('emoji', '📦')
        stars = p.get('stars', p.get('stars_delta', p.get('stars_per_day', 'N/A')))
        if isinstance(stars, int):
            stars = f"{stars:,} stars/day"
        desc = (p.get('desc', p.get('description', '')) or '')[:120]
        language = p.get('language', '')
        verdict = p.get('verdict', '')
        last_seen = p.get('last_seen_date', '')
        has_profile = p.get('_has_profile', False)

        # Build tags from language + verdict + category
        tags = []
        if language:
            tags.append(language)
        if verdict and '⭐' in verdict:
            tags.append('重点跟踪')
        category = p.get('category', '')
        if category:
            tags.append(category)
        if not tags:
            tags = ['项目']

        # Build href: link to profile page if exists, else to the daily page where last seen
        if has_profile:
            slug = make_slug(name)
            href = f"projects/{slug}.html"
        else:
            href = f"daily/{last_seen}.html"

        tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags[:3]])
        seen_html = f'<div style="font-size:12px;color:var(--text-muted);margin-top:4px;">最近出现: {last_seen}</div>' if last_seen else ''

        cards += f'''                <a href="/github-researcher/{href}" class="card">
                    <div class="card-top">
                        <div class="card-emoji">{emoji}</div>
                        <div class="card-stars">{stars}</div>
                    </div>
                    <div class="card-title">{name}</div>
                    <div class="card-desc">{desc}</div>
                    <div class="card-tags">{tag_html}</div>
                    {seen_html}
                </a>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>重点项目 | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>⭐</text></svg>">
{CSS}
    <style>
        .page-header {{ padding: 48px 0 36px; text-align: center; }}
        .page-header h1 {{ font-size: 36px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 12px; }}
        .page-header p {{ color: var(--text-muted); font-size: 16px; }}
        .card-grid {{ animation: none; }}
    </style>
</head>
<body>
{NAV.replace('id="nav-projects"', 'id="nav-projects" class="active"')}
<main class="container">
    <div class="page-header">
        <h1>⭐ 重点项目</h1>
        <p>聚合自所有日报的深度分析项目,持续跟踪</p>
    </div>
    <div class="card-grid">
{cards}
    </div>
</main>
{FOOTER}
</body>
</html>'''

    with open(os.path.join(DOCS_DIR, 'projects.html'), 'w') as f:
        f.write(html)
    print(f"Generated projects.html with {len(all_projects)} projects")


# === Generate individual project page ===
def generate_project_page(filepath):
    raw_name = os.path.basename(filepath).replace('.md', '')
    slug = make_slug(raw_name)

    with open(filepath, 'r') as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    html_body = markdown.markdown(body, extensions=['tables', 'toc'])

    title = fm.get('title', raw_name)

    project_style = '''
    <style>
        .project-content { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 40px 48px; box-shadow: var(--shadow); margin-bottom: 48px; max-width: 860px; margin-left: auto; margin-right: auto; }
        .project-content h1 { font-size: 26px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 6px; }
        .project-content h2 { font-size: 18px; font-weight: 700; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 12px; margin: 28px 0 14px; }
        .project-content h3 { font-size: 15px; font-weight: 700; color: var(--text); margin: 20px 0 10px; }
        .project-content table { border-collapse: collapse; width: 100%; margin: 14px 0; }
        .project-content th, .project-content td { border: 1px solid var(--border); padding: 8px 12px; text-align: left; font-size: 13px; }
        .project-content th { background: var(--primary); color: white; font-weight: 600; }
        .project-content tr:nth-child(even) td { background: var(--bg); }
        .project-content blockquote { background: linear-gradient(135deg, #F3E8FF, #ECFEFF); border-left: 4px solid var(--primary); padding: 14px 18px; margin: 14px 0; border-radius: 0 8px 8px 0; }
        .project-content ul, .project-content ol { padding-left: 22px; margin: 10px 0; }
        .project-content li { margin: 6px 0; font-size: 14px; }
        .project-content p { font-size: 14px; margin-bottom: 12px; line-height: 1.7; }
        .project-content strong { color: var(--primary-dark); }
        .back-link { display: inline-flex; align-items: center; gap: 6px; color: var(--primary); text-decoration: none; font-size: 14px; font-weight: 500; margin-bottom: 24px; }
        .back-link:hover { text-decoration: underline; }
    </style>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>⭐</text></svg>">
{CSS}
    {project_style}
</head>
<body>
{NAV.replace('id="nav-projects"', 'id="nav-projects" class="active"')}
<main class="container">
    <a href="/github-researcher/projects.html" class="back-link">← 返回重点项目</a>
    <div class="project-content">
        {html_body}
    </div>
</main>
{FOOTER}
</body>
</html>'''

    proj_html_dir = os.path.join(DOCS_DIR, 'projects')
    os.makedirs(proj_html_dir, exist_ok=True)
    with open(os.path.join(proj_html_dir, f'{slug}.html'), 'w') as f:
        f.write(html)
    print(f"Generated projects/{slug}.html")


def make_slug(name):
    """Generate project slug: remove parenthesized content, lowercase, replace non-alnum with -."""
    s = re.sub(r'\s*\([^)]*\)\s*', '', name).strip()
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def generate_minimal_project_page(name, data, date_str):
    """Generate a minimal project detail page from daily report data."""
    slug = make_slug(name)
    proj_html_dir = os.path.join(DOCS_DIR, 'projects')
    os.makedirs(proj_html_dir, exist_ok=True)
    filepath = os.path.join(proj_html_dir, f'{slug}.html')

    url = data.get('url', '')
    desc = data.get('description', data.get('desc', ''))
    language = data.get('language', '')
    stars = data.get('stars', '')
    stars_delta = data.get('stars_delta', '')
    analysis = data.get('analysis', '')
    verdict = data.get('verdict', '')

    tags = []
    if language:
        tags.append(language)
    if verdict and '⭐' in verdict:
        tags.append('重点跟踪')
    tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags])

    meta_lines = ''
    if stars:
        meta_lines += f'<p><strong>Stars:</strong> {stars}</p>'
    if stars_delta:
        meta_lines += f'<p><strong>增速:</strong> {stars_delta}</p>'
    if url:
        meta_lines += f'<p><strong>GitHub:</strong> <a href="{url}" target="_blank">{url}</a></p>'
    if language:
        meta_lines += f'<p><strong>语言:</strong> {language}</p>'
    if verdict:
        meta_lines += f'<p><strong>判断:</strong> {verdict}</p>'
    if date_str:
        meta_lines += f'<p><strong>来源日报:</strong> <a href="/github-researcher/daily/{date_str}.html">{date_str}</a></p>'

    analysis_html = f'<h2>分析</h2>\n<p>{analysis}</p>' if analysis else ''

    body_html = f'''<h1>{name}</h1>
<div class="card-tags" style="margin-bottom:20px;">{tag_html}</div>
{meta_lines}
<h2>简介</h2>
<p>{desc}</p>
{analysis_html}'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>⭐</text></svg>">
{CSS}
    <style>
        .project-content {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 40px 48px; box-shadow: var(--shadow); margin-bottom: 48px; max-width: 860px; margin-left: auto; margin-right: auto; }}
        .project-content h1 {{ font-size: 26px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 6px; }}
        .project-content h2 {{ font-size: 18px; font-weight: 700; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 12px; margin: 28px 0 14px; }}
        .project-content p {{ font-size: 14px; margin-bottom: 12px; line-height: 1.7; }}
        .project-content a {{ color: var(--primary); }}
        .back-link {{ display: inline-flex; align-items: center; gap: 6px; color: var(--primary); text-decoration: none; font-size: 14px; font-weight: 500; margin-bottom: 24px; }}
        .back-link:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
{NAV.replace('id="nav-projects"', 'id="nav-projects" class="active"')}
<main class="container">
    <a href="/github-researcher/trends.html" class="back-link">← 返回趋势时间线</a>
    <div class="project-content">
        {body_html}
    </div>
</main>
{FOOTER}
</body>
</html>'''

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"  Generated minimal project page: projects/{slug}.html")
    return slug


# === Generate trends page ===
def generate_trends():
    daily_files = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True)

    # Build set of existing project slugs from projects/*.md
    existing_slugs = set()
    for pf in glob.glob(os.path.join(PROJECTS_DIR, '*.md')):
        existing_slugs.add(make_slug(os.path.basename(pf).replace('.md', '')))

    # Also check docs/projects/*.html for already-generated minimal pages
    existing_html_slugs = set()
    for pf in glob.glob(os.path.join(DOCS_DIR, 'projects', '*.html')):
        existing_html_slugs.add(make_slug(os.path.basename(pf).replace('.html', '')))

    date_sections = ''
    idx = 0

    for df in daily_files:
        date_str = os.path.basename(df).replace('.md', '')
        with open(df, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        summary = fm.get('summary', '')
        trends = fm.get('trends', []) or []
        key_projects = fm.get('key_projects', []) or []

        is_first = (idx == 0)
        date_sections += f'''
        <div class="date-section">
            <div class="date-toggle" onclick="toggleSection('ds-{date_str}')" style="cursor:pointer;">
                <div class="date-header">
                    <span class="date-badge">{date_str}</span>
                    <span class="date-summary">{summary}</span>
                    <span class="date-arrow" id="arrow-ds-{date_str}">{'▼' if is_first else '▶'}</span>
                </div>
            </div>
            <div class="date-trends" id="ds-{date_str}" style="{'display:block;' if is_first else 'display:none;'}">
'''

        # Trend directions
        if trends:
            date_sections += '<div style="margin-bottom:16px;">'
            for t in trends:
                rank = t.get('rank', 0)
                name = t.get('name', 'Unknown')
                score_val = t.get('score', 0)
                is_high = score_val >= 55 if isinstance(score_val, int) else False
                rank_class = 'top' if rank <= 2 else ''
                score_class = 'high' if is_high else ''
                date_sections += f'''
                <div class="trend-item">
                    <div class="trend-rank {rank_class}">{rank}</div>
                    <div class="trend-content">
                        <div class="trend-title">{name}</div>
                    </div>
                    <div class="trend-score {score_class}">{score_val}/80</div>
                </div>'''
            date_sections += '</div>'

        # Key projects as cards
        if key_projects:
            date_sections += '<div class="section-title" style="margin-bottom:12px;"><span>🎯 重点项目</span></div>\n'
            date_sections += '<div class="card-grid" style="animation:none;margin-bottom:8px;">\n'
            for p in key_projects:
                pname = p.get('name', 'Unknown')
                slug = make_slug(pname)
                desc = (p.get('description', p.get('desc', '')) or '')[:80]
                language = p.get('language', '')
                stars = p.get('stars', p.get('stars_delta', ''))
                verdict = p.get('verdict', '')

                # Check if project page exists
                if slug not in existing_slugs and slug not in existing_html_slugs:
                    generate_minimal_project_page(pname, p, date_str)
                    existing_html_slugs.add(slug)

                tags = []
                if language:
                    tags.append(language)
                if verdict and '⭐' in verdict:
                    tags.append('重点跟踪')
                if not tags:
                    tags = ['项目']
                tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags[:3]])

                date_sections += f'''
                <a href="/github-researcher/projects/{slug}.html" class="card">
                    <div class="card-top">
                        <div class="card-emoji">📦</div>
                        <div class="card-stars">{stars}</div>
                    </div>
                    <div class="card-title">{pname}</div>
                    <div class="card-desc">{desc}</div>
                    <div class="card-tags">{tag_html}</div>
                </a>'''
            date_sections += '</div>\n'

        date_sections += '''
            </div>
        </div>
'''
        idx += 1

    toggle_js = '''
    <script>
    function toggleSection(id) {
        var el = document.getElementById(id);
        var arrow = document.getElementById('arrow-' + id);
        if (el.style.display === 'none') {
            el.style.display = 'block';
            arrow.textContent = '▼';
        } else {
            el.style.display = 'none';
            arrow.textContent = '▶';
        }
    }
    </script>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>趋势时间线 | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📈</text></svg>">
{CSS}
    <style>
        .page-header {{ padding: 48px 0 36px; text-align: center; }}
        .page-header h1 {{ font-size: 36px; font-weight: 800; background: linear-gradient(135deg, var(--primary-dark), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 12px; }}
        .page-header p {{ color: var(--text-muted); font-size: 16px; }}
        .date-section {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; margin-bottom: 16px; box-shadow: var(--shadow); }}
        .date-header {{ display: flex; align-items: center; gap: 12px; padding: 16px 20px; transition: background 0.15s; }}
        .date-toggle:hover .date-header {{ background: var(--bg); }}
        .date-badge {{ background: linear-gradient(135deg, var(--primary), var(--primary-light)); color: white; padding: 4px 12px; border-radius: 100px; font-size: 13px; font-weight: 700; white-space: nowrap; }}
        .date-summary {{ flex: 1; font-size: 14px; color: var(--text); font-weight: 500; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
        .date-arrow {{ color: var(--text-muted); font-size: 12px; }}
        .date-trends {{ padding: 0 20px 16px; }}
        .section-title {{ display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 700; color: var(--text); }}
    </style>
</head>
<body>
{NAV.replace('id="nav-trends"', 'id="nav-trends" class="active"')}
<main class="container">
    <div class="page-header">
        <h1>📈 Trend Timeline</h1>
        <p>按日期浏览每日 GitHub 趋势研究报告</p>
    </div>
{date_sections}
</main>
{FOOTER}
{toggle_js}
</body>
</html>'''

    with open(os.path.join(DOCS_DIR, 'trends.html'), 'w') as f:
        f.write(html)
    print(f"Generated trends.html with {len(daily_files)} daily entries")


# === Main ===
if __name__ == '__main__':
    print("Generating GitHub Pages HTML...")
    generate_index()
    generate_daily_list()

    for df in sorted(glob.glob(os.path.join(DAILY_DIR, '*.md'))):
        generate_daily_page(df)

    generate_projects_list()

    for pf in sorted(glob.glob(os.path.join(PROJECTS_DIR, '*.md'))):
        generate_project_page(pf)

    generate_trends()
    print("Done! All HTML pages generated.")
