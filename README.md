# micropython-hw-lib
Micropython (ESP8266) library for hardware peripherals.
The collection includes external repositories, therefore it is required to run `git submodule update --init` after cloning repository.

## Usage
The scripts are simple python modules that should be placed directly into micropython filesystem and imported, e.g: 

`from pcf8574 import PCF8574`.

To save some space and time at import, individual files can be cross-compiled prior to transfering them to filesystem. This will generate micropython bytecode `.mpy` files that can be imported just like normal scripts with command above. The cross-compiler is part of micropython source and first needs to be built. Aftwerwards, it can be used like this:

`MICROPYTHON_ROOT_DIR/mpy-cross/mpy-cross pcf8574.py`

However, these files still reside in filesystem. To optimize further, they can be "freezed" (saved) into Flash memory. This will make them permanent part of the micropython binary. This can be done by placing them inside target's `modules` or `scripts` folder, e.g:

`MICROPYTHON_ROOT_DIR/esp8266/modules/`

`MICROPYTHON_ROOT_DIR/esp8266/scripts/`

The difference between the two is that scripts in `modules` folder gets compiled into bytecode with `mpy-cross` tool like above, while those in `scripts` will be just freezed into Flash. Note that only `.py` scripts should be placed in both folders as anything else can cause firmware corruption. After placing scripts in either of them, rebuild is needed. This will generate new firmware image that can be flashed like usual. The scripts are immediately available using the `import` syntax from above.
