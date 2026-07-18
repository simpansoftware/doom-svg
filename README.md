# DOOM-SVG
It's DOOM, ported to a SVG using Emscripten.
## How do I run this?
- Running precompiled
    - Go to https://simpansoftware.cc/doom-svg/doom.svg on a pc via a web browser, and that's DOOM!
    - Alternatively open doom.svg from this repo.
- Compiling and then running
    - Requirements: Python
    - Run the following 
    ```git clone https://github.com/simpansoftware/doom-svg
    cd build
    python3 build.py
    ```
    - After that, open up doom.svg in the build folder in the browser and you should be running DOOM from a freshly built SVG!
## What makes this any different than Chris Dalke's SVG DOOM port?
His SVG DOOM port shows that JS-DOS can run inside an SVG, and while that's impressive, it still relies on downloading DOOM from an external server.<br>
My project uses an Emscripten port of DOOM and runs completely standalone. The game data, the game code and the WebAssembly are all embedded into `doom.svg`, so no external downloading is required.<br>
This means that you can just open doom.svg in a browser while offline, and it would work
## Controls?
- Arrow keys or WASD to move
- Shift to sprint
- Space to interact with doors etc
- CTRL or Left Mouse button to shoot (note: mouse movement doesnt work due to my emscripten port lacking it) 
## What did I learn?
I learnt the following
- That foreignObject exists in SVGs and is basically just HTML but worse if you style it correctly
- That Chris Dalke made a DOOM port for SVGs before in a different way
- How to bundle JS in SVGs
## What needs to be done:
- Better website
- Add mouse movement same way how i added WASD support
## Credits
- Me for making the initial svg port
- Claude for helping with the js override in the compiler to make it a one file doom.svg
- ading2210 for the inspiration from DOOMPDF