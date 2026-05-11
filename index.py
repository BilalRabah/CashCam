from http.server import BaseHTTPRequestHandler

# كود الواجهة الشكاكي (TikTok Style)
tiktok_ui = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CashCam - Reels</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background-color: #000; font-family: sans-serif; overflow: hidden; }
        
        /* حاوية الفيديوهات */
        .video-container {
            height: 100vh;
            scroll-snap-type: y mandatory;
            overflow-y: scroll;
        }
        
        .video-card {
            height: 100vh;
            width: 100%;
            scroll-snap-align: start;
            position: relative;
            background: linear-gradient(to bottom, #111, #333);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* محاكاة الفيديو */
        .video-placeholder {
            color: #555;
            font-size: 20px;
            text-align: center;
        }

        /* الأزرار الجانبية */
        .side-bar {
            position: absolute;
            right: 15px;
            bottom: 100px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-items: center;
        }

        .icon {
            width: 45px;
            height: 45px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
        }

        .icon span { font-size: 12px; margin-top: 5px; }

        /* معلومات الفيديو بالأسفل */
        .video-info {
            position: absolute;
            bottom: 30px;
            left: 15px;
            color: white;
            text-align: left;
            width: 80%;
        }

        .username { font-weight: bold; margin-bottom: 10px; font-size: 18px; color: #38bdf8; }
        .description { font-size: 14px; line-height: 1.4; opacity: 0.9; }

        /* الهيدر العلوي */
        .top-nav {
            position: absolute;
            top: 20px;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 20px;
            color: white;
            font-weight: bold;
            z-index: 10;
            opacity: 0.7;
        }
    </style>
</head>
<body>

    <div class="top-nav">
        <span>متابعة</span>
        <span style="border-bottom: 2px solid white;">لك</span>
    </div>

    <div class="video-container">
        <div class="video-card">
            <div class="video-placeholder">🎥 فيديو رقم 1 (CashCam)</div>
            <div class="side-bar">
                <div class="icon">❤️</div>
                <div class="icon">💬</div>
                <div class="icon">🔗</div>
            </div>
            <div class="video-info">
                <div class="username">@Bilal_Rabah</div>
                <div class="description">أهلاً بكم في CashCam! أول تطبيق ذكي لمعالجة البيانات بالذكاء الاصطناعي 🚀 #تكنولوجيا #العراق</div>
            </div>
        </div>

        <div class="video-card" style="background: linear-gradient(to bottom, #001f3f, #000);">
            <div class="video-placeholder">🎥 فيديو رقم 2 (الذكاء الاصطناعي)</div>
            <div class="side-bar">
                <div class="icon">❤️</div>
                <div class="icon">💬</div>
                <div class="icon">🔗</div>
            </div>
            <div class="video-info">
                <div class="username">@CashCam_AI</div>
                <div class="description">شاهد كيف يقوم النظام بتحليل التربة والمباني بدقة عالية جداً 🔥 #هندسة #ذكاء_اصطناعي</div>
            </div>
        </div>
    </div>

</body>
</html>
"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(tiktok_ui.encode('utf-8'))
        return
