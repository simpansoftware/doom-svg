import pathlib

template = pathlib.Path("template.svg").read_text(encoding="utf-8")
js = pathlib.Path("index.js").read_text(encoding="utf-8")
wasm = pathlib.Path("wasm.b64").read_text(encoding="utf-8").strip()
data = pathlib.Path("data.b64").read_text(encoding="utf-8").strip()

emscriptenOverride = f"""
window.Module = window.Module || {{}};
Module.locateFile = function(path, prefix) {{
    if (path === 'index.data') {{
        return 'data:application/octet-stream;base64,{data}';
    }}
    if (path.endsWith('.wasm')) {{
        return 'data:application/wasm;base64,{wasm}';
    }}
    return (prefix || '') + path;
}};""" # override coded partly by claude, as im terrible at js

combined = emscriptenOverride + "\n" + js
inject = f"<script><![CDATA[{combined}]]></script>"
output = template.replace("</body>", f"{inject}\n</body>")
pathlib.Path("doom.svg").write_text(output, encoding="utf-8")
print("done!")