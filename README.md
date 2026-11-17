# Cyber attacks & outages: Aug 17 – Nov 17, 2026

**Live site: https://clau5.github.io/outage-timeline-2026/**

An interactive timeline of 99 verified cyber attacks, system outages and service disruptions between August 17 and November 17, 2026. It covers cloud, SaaS, banking, aviation, government, telecom, payments and DNS/PKI.

## What's inside
- **Two-year trend (Nov 2024 – Nov 2026):** four independent monthly series (ransomware leak-site victims, ThousandEyes network outage events, CISA KEV additions, NVD CVEs published), each with a 3-month rolling average and an indexed view, plus a verdict on whether the last three months are above trend.
- **Major vulnerabilities:** PHP2Shell, Node2Shell, NetScaler, Ivanti, Fragnesia and others, kept separate from incident counts.
- **Timeline:** every incident by date, coloured by officially stated cause (Attack, Spoof-Error, Maintenance, Unknown) and sized by severity (1–5). Tap a dot for details and the source.
- **Filters:** by cause and sector, applied to the timeline, the table and the weekly chart.
- **Sortable table:** all incidents with a source link for each one.
- **Weekly frequency:** stacked bars per ISO week, by cause.
- **Year over year:** mid-Aug to mid-Nov, 2025 vs 2026, from sources that report both years (ThousandEyes outage events +134%, ransomware leak-site victims +48%, GitHub incidents +50%), with caveats.
- **November spike:** what happened Nov 12–17, when 14 incidents landed in six days.
- **Disputed causes:** where official explanations are thin or sources disagree.

## Files
- `index.html`: the site. Self-contained, plain JS/SVG, no dependencies. The table is pre-rendered.
- `trend.json`: monthly trend series. `vulns.json`: major vulnerabilities.
- `data.json`: the incident dataset (date, org, sector, incident, cause, severity, severity_note, source, flag).
- `template.html` + `build.py`: regenerate `index.html` from `data.json` with `python3 build.py`.

## Notes
Causes are as officially stated by the affected organisations or authorities at the time of writing, and may change as investigations conclude. Severity is an editorial judgement. Last updated Nov 17, 2026.
