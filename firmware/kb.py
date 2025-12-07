import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide

class NibunkatsuOne(KMKKeyboard):
    def __init__(self):
        # --- Matrix Setup ---
        # Pins from your Schematic (IO4-IO7 Rows, IO15-IO14 Cols)
        self.row_pins = (board.IO4, board.IO5, board.IO6, board.IO7)
        self.col_pins = (board.IO15, board.IO16, board.IO17, board.IO18, board.IO21, board.IO14)
        
        # You confirmed: Cathode to Row -> ROW2COL
        self.diode_orientation = DiodeOrientation.ROW2COL

        # --- Split Communication (TRRS) ---
        # Because you crossed the traces on the Right PCB, 
        # we use the SAME pin definitions for both chips!
        self.split = Split(
            split_type=SplitType.UART,
            data_pin=board.IO37,  # TX Pin (Tip on Left, Ring on Right)
            data_pin2=board.IO36, # RX Pin (Ring on Left, Tip on Right)
            uart_flip=True,       # Helps ESP32 negotiate the connection
            use_pio=True          # Uses dedicated hardware for stability
        )
        self.modules.append(self.split)
        
        # --- RGB Data Pin ---
        # We moved this to IO10 to save USB
        self.rgb_pixel_pin = board.IO10
        
        # --- Encoder Pins (Right Side) ---
        # Update these if you routed them differently!
        self.encoder_a = board.IO8 
        self.encoder_b = board.IO9 

        # Call the parent init
        super().__init__()