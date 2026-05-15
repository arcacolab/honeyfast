import os
import server
from aiohttp import web

WEB_DIR = os.path.dirname(__file__)

@server.PromptServer.instance.routes.get("/honeyfast")
async def serve_ui(request):
    html_path = os.path.join(WEB_DIR, "index.html")
    if not os.path.exists(html_path):
        return web.Response(text="index.html 없음", status=404)
    return web.FileResponse(html_path)

@server.PromptServer.instance.routes.get("/honeyfast/tags.csv")
async def serve_csv(request):
    csv_path = os.path.join(WEB_DIR, "tags.csv")
    if not os.path.exists(csv_path):
         return web.Response(text="", status=404)
    return web.FileResponse(csv_path)

# JSON 워크플로우 파일을 서빙하기 위한 라우트 추가!
@server.PromptServer.instance.routes.get("/honeyfast/fast_mod_new.json")
async def serve_workflow(request):
    json_path = os.path.join(WEB_DIR, "fast_mod_new.json")
    if not os.path.exists(json_path):
        return web.Response(text="fast_mod_new.json 없음", status=404)
    return web.FileResponse(json_path)

NODE_CLASS_MAPPINGS = {}
