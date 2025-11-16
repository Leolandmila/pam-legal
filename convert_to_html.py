#!/usr/bin/env python3
"""
Convert Markdown legal documents to HTML for web hosting
"""

import re

def markdown_to_html(md_content, title):
    """Convert basic Markdown to HTML"""
    html = md_content

    # Convert headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Convert bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

    # Convert italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Convert links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)

    # Convert bullet points
    lines = html.split('\n')
    in_list = False
    new_lines = []

    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
            new_lines.append(f'<li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            new_lines.append(line)

    if in_list:
        new_lines.append('</ul>')

    html = '\n'.join(new_lines)

    # Convert paragraphs (lines not already in tags)
    lines = html.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('<') and not stripped.endswith('>'):
            new_lines.append(f'<p>{line}</p>')
        else:
            new_lines.append(line)

    html = '\n'.join(new_lines)

    # Create full HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Parent Admin Manager</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.7;
            color: #333;
            background: #fff;
        }}
        h1 {{
            color: #7D0820;
            border-bottom: 3px solid #7D0820;
            padding-bottom: 15px;
            margin-bottom: 30px;
            font-size: 2.5em;
        }}
        h2 {{
            color: #7D0820;
            margin-top: 40px;
            margin-bottom: 15px;
            font-size: 1.8em;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 10px;
        }}
        h3 {{
            color: #555;
            margin-top: 30px;
            margin-bottom: 12px;
            font-size: 1.4em;
        }}
        h4 {{
            color: #666;
            margin-top: 25px;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        p {{
            margin: 15px 0;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        a {{
            color: #7D0820;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        strong {{
            font-weight: 600;
            color: #000;
        }}
        em {{
            font-style: italic;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        .header-links {{
            text-align: center;
            margin-bottom: 30px;
            padding: 15px;
            background: #f8f8f8;
            border-radius: 8px;
        }}
        .header-links a {{
            margin: 0 15px;
            font-weight: 500;
        }}
        footer {{
            margin-top: 60px;
            padding-top: 30px;
            border-top: 2px solid #ddd;
            text-align: center;
            color: #666;
            font-size: 14px;
        }}
        .back-link {{
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #7D0820;
            color: white;
            border-radius: 6px;
            text-decoration: none;
        }}
        .back-link:hover {{
            background: #5a0617;
            text-decoration: none;
        }}
        @media (max-width: 600px) {{
            body {{
                padding: 20px 15px;
            }}
            h1 {{
                font-size: 2em;
            }}
            h2 {{
                font-size: 1.5em;
            }}
        }}
    </style>
</head>
<body>
    <div class="header-links">
        <a href="index.html">Home</a>
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms-of-service.html">Terms of Service</a>
    </div>

    {html}

    <footer>
        <p><strong>Last Updated:</strong> November 16, 2025</p>
        <p>For questions, contact: <a href="mailto:privacy@parentaladminmanager.com">privacy@parentaladminmanager.com</a></p>
        <a href="index.html" class="back-link">← Back to Legal Documents</a>
        <p style="margin-top: 30px; font-style: italic;">Parent Admin Manager - Your Family's Privacy is Our Priority</p>
    </footer>
</body>
</html>"""

    return full_html


def main():
    import os

    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)

    # Read Privacy Policy
    with open(os.path.join(parent_dir, 'PRIVACY_POLICY.md'), 'r') as f:
        privacy_md = f.read()

    # Read Terms of Service
    with open(os.path.join(parent_dir, 'TERMS_OF_SERVICE.md'), 'r') as f:
        terms_md = f.read()

    # Convert to HTML
    privacy_html = markdown_to_html(privacy_md, 'Privacy Policy')
    terms_html = markdown_to_html(terms_md, 'Terms of Service')

    # Write HTML files
    with open(os.path.join(base_dir, 'public', 'privacy-policy.html'), 'w') as f:
        f.write(privacy_html)

    with open(os.path.join(base_dir, 'public', 'terms-of-service.html'), 'w') as f:
        f.write(terms_html)

    print("✅ Successfully converted legal documents to HTML!")
    print(f"   - privacy-policy.html")
    print(f"   - terms-of-service.html")
    print(f"\nFiles are in: {os.path.join(base_dir, 'public')}")


if __name__ == '__main__':
    main()
