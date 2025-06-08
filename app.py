from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# For deployment - use relative paths
static_path = os.path.join(os.path.dirname(__file__), 'static')
os.makedirs(static_path, exist_ok=True)

# Campaign data
CAMPAIGN_MATERIALS = [
    {
        "id": 1,
        "title": "LinkedIn Awareness Post",
        "description": "Clean aesthetics showing coffee pouring action creates professional appeal while demonstrating product integration on LinkedIn. This positions Minor Figures as the sophisticated choice for coffee culture enthusiasts.",
        "stage": "Awareness - Coffee Culture Discovery",
        "image": "F1.png"
    },
    {
        "id": 2,
        "title": "Instagram Stories Collection",
        "description": "Multi-panel brand showcase effectively demonstrates product versatility across different contexts. The varied lifestyle moments build emotional connection and show authentic usage scenarios.",
        "stage": "Awareness/Consideration - Product Education",
        "image": "F2.png"
    },
    {
        "id": 3,
        "title": "Social Media Campaign Ad",
        "description": "Bold film strip design with vibrant colors creates eye-catching promotional content. The creative \"FREEE\" typography and discount offer drives immediate action while maintaining brand playfulness.",
        "stage": "Purchase - Conversion incentive",
        "image": "F3.png"
    },
    {
        "id": 4,
        "title": "Product Lifestyle Posts",
        "description": "Six-panel grid demonstrates comprehensive brand integration across coffee culture touchpoints. This builds credibility by showing real-world usage and professional applications.",
        "stage": "Consideration - Community Building",
        "image": "F4.png"
    },
    {
        "id": 5,
        "title": "Brand Values Ad",
        "description": "The pastoral illustration with the cow creates emotional storytelling around dairy-free messaging (created with AI). This clever visual metaphor communicates sustainability values while maintaining an approachable, friendly brand personality.",
        "stage": "Awareness - Sustainability messaging",
        "image": "F5.png"
    },
    {
        "id": 6,
        "title": "Interactive QR Campaign",
        "description": "Minimalist design featuring scannable QR code that links directly to Minor Figures website creates a seamless digital bridge. This innovative approach transforms traditional advertising into immediate engagement opportunities.",
        "stage": "Purchase - Digital engagement bridge",
        "image": "F6.png"
    },
    {
        "id": 7,
        "title": "Digital Identity Campaign",
        "description": "Artistic portrait with integrated QR code (linking to website) targets tech-savvy consumers. This creates memorable brand identity while providing instant access to digital touchpoints.",
        "stage": "Retention - Community identity",
        "image": "F7.png"
    },
    {
        "id": 8,
        "title": "Product Hero Shot",
        "description": "Clean carton design featuring signature duck mascot with a generated QR code (linking to website) emphasizes barista-quality positioning. The character branding creates memorable visual identity while enabling instant digital engagement.",
        "stage": "Consideration - Product education",
        "image": "F8.png"
    },
    {
        "id": 9,
        "title": "Lifestyle Illustration",
        "description": "Artistic duck character in streetwear with QR codes (actively links to the website) appeals to younger demographics. This builds brand personality through relatable character design while maintaining premium positioning.",
        "stage": "Retention - Brand personality",
        "image": "F9.png"
    },
    {
        "id": 10,
        "title": "Email Newsletter Header",
        "description": "Weekly coffee expertise newsletter featuring barista tips, product highlights, and sustainability messaging to build customer loyalty and position Minor Figures as the coffee professional's trusted partner.",
        "stage": "Retention - Expert content delivery and community building",
        "image": "F10.png"
    }
]

@app.route('/')
def dashboard():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minor Figures Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #f5f3f0 0%, #ebe7e0 100%);
            min-height: 100vh;
            color: #4a4a4a;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
        }

        .brand-title {
            font-size: 3rem;
            font-weight: 300;
            letter-spacing: 8px;
            color: #2c2c2c;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }

        .subtitle {
            font-size: 1.1rem;
            color: #8b8680;
            font-weight: 300;
            letter-spacing: 2px;
        }

        .dashboard-content {
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .image-container {
            text-align: center;
            margin-bottom: 2rem;
        }

        .main-image {
            max-width: 100%;
            height: auto;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .main-image:hover {
            transform: scale(1.02);
        }

        .interactive-section {
            margin: 3rem 0;
            text-align: center;
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 300;
            color: #2c2c2c;
            margin-bottom: 1.5rem;
            letter-spacing: 2px;
        }

        .campaign-button {
            display: inline-block;
            background: rgba(255, 255, 255, 0.8);
            color: #2c2c2c;
            padding: 1.2rem 2.5rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 400;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            border: 1px solid rgba(200, 190, 180, 0.3);
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        }

        .campaign-button:hover {
            background: rgba(255, 255, 255, 0.95);
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
            color: #1a1a1a;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.5);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(200, 190, 180, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }

        .stat-number {
            font-size: 2.5rem;
            font-weight: 200;
            color: #3c3c3c;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #8b8680;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            color: #a09a94;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .brand-title {
                font-size: 2rem;
                letter-spacing: 4px;
            }

            .container {
                padding: 1rem;
            }

            .dashboard-content {
                padding: 2rem;
            }

            .stats-grid {
                grid-template-columns: 1fr;
                gap: 1rem;
            }

            .campaign-button {
                padding: 1rem 2rem;
                font-size: 0.9rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="brand-title">Minor Figures</h1>
            <p class="subtitle">Dashboard</p>
        </div>

        <div class="dashboard-content">
            <div class="image-container">
                <img src="/static/F6.png" alt="Minor Figures" class="main-image">
            </div>

            <div class="interactive-section">
                <h2 class="section-title">Explore Campaign Strategy</h2>
                <a href="/campaigns" class="campaign-button">View All Campaign Recommendations</a>
            </div>

            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">Quality</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Available</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">∞</div>
                    <div class="stat-label">Possibilities</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">2025</div>
                    <div class="stat-label">Innovation</div>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>Minor Figures Dashboard • Minimalist Design • Modern Interface</p>
        </div>
    </div>
</body>
</html>
    """
    return html_content

@app.route('/campaigns')
def campaigns():
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minor Figures Campaign Recommendations</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #f5f3f0 0%, #ebe7e0 100%);
            min-height: 100vh;
            color: #4a4a4a;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .header {{
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
        }}

        .brand-title {{
            font-size: 3rem;
            font-weight: 300;
            letter-spacing: 8px;
            color: #2c2c2c;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }}

        .subtitle {{
            font-size: 1.1rem;
            color: #8b8680;
            font-weight: 300;
            letter-spacing: 2px;
        }}

        .back-button {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.8);
            color: #2c2c2c;
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 400;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            border: 1px solid rgba(200, 190, 180, 0.3);
            backdrop-filter: blur(10px);
            margin-bottom: 2rem;
        }}

        .back-button:hover {{
            background: rgba(255, 255, 255, 0.95);
            transform: translateY(-2px);
        }}

        .campaigns-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2.5rem;
            margin-bottom: 4rem;
        }}

        .campaign-card {{
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.5);
            transition: all 0.3s ease;
            position: relative;
            display: flex;
            flex-direction: column;
        }}

        .campaign-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 35px 70px rgba(0, 0, 0, 0.12);
        }}

        .card-number {{
            position: absolute;
            top: 1.5rem;
            left: 1.5rem;
            background: rgba(255, 255, 255, 0.9);
            color: #4a4a4a;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 1.1rem;
            z-index: 2;
            backdrop-filter: blur(10px);
        }}

        .image-container {{
            position: relative;
            min-height: 200px;
            max-height: 400px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(248, 246, 243, 0.8);
            padding: 1rem;
        }}

        .campaign-image {{
            max-width: 100%;
            max-height: 100%;
            width: auto;
            height: auto;
            object-fit: contain;
            transition: transform 0.3s ease;
            border-radius: 8px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        }}

        .campaign-card:hover .campaign-image {{
            transform: scale(1.02);
        }}

        .card-content {{
            padding: 2rem;
        }}

        .campaign-title {{
            font-size: 1.4rem;
            font-weight: 500;
            color: #2c2c2c;
            margin-bottom: 0.8rem;
            letter-spacing: 1px;
        }}

        .journey-stage {{
            display: inline-block;
            background: rgba(139, 134, 128, 0.1);
            color: #6b6560;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.8rem;
            font-weight: 500;
            letter-spacing: 0.5px;
            margin-bottom: 1rem;
            text-transform: uppercase;
        }}

        .campaign-description {{
            color: #5a5a5a;
            font-size: 0.95rem;
            line-height: 1.7;
        }}

        @media (max-width: 768px) {{
            .brand-title {{
                font-size: 2rem;
                letter-spacing: 4px;
            }}
            
            .campaigns-grid {{
                grid-template-columns: 1fr;
                gap: 2rem;
            }}
            
            .container {{
                padding: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="/" class="back-button">← Back to Dashboard</a>
            <h1 class="brand-title">Minor Figures</h1>
            <p class="subtitle">Campaign Recommendations</p>
        </div>

        <div class="campaigns-grid">
"""

    for campaign in CAMPAIGN_MATERIALS:
        html_content += f"""
            <div class="campaign-card">
                <div class="card-number">{campaign['id']}</div>
                <div class="image-container">
                    <img src="/static/{campaign['image']}" alt="{campaign['title']}" class="campaign-image">
                </div>
                <div class="card-content">
                    <h3 class="campaign-title">{campaign['title']}</h3>
                    <div class="journey-stage">{campaign['stage']}</div>
                    <p class="campaign-description">{campaign['description']}</p>
                </div>
            </div>
"""

    html_content += """
        </div>
    </div>
</body>
</html>
    """
    return html_content

@app.route('/static/<filename>')
def static_files(filename):
    return send_from_directory(static_path, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6300))
    app.run(debug=False, host='0.0.0.0', port=port)
