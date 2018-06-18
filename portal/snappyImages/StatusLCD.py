from synapse.switchboard import * 

PIN_CS = 15
PIN_BUSY = 16
PIN_BUTTON = 17
PIN_UNUSED = 18

bootWait = 20 # 2 seconds

sequenceA = None
seq_posA = 0
seq_countA = ""

sequenceB = None
seq_posB = 0
seq_countB = ""

@setHook(HOOK_STARTUP)
def _startupEvent():
    
    #crossConnectForProgramming()
    #usingPropPlug()
    #return
    
    initUart(0, 57600)            # UART0 at 57600
    flowControl(0, False)         # Character mode, no echo 
    
    crossConnect(DS_UART0,DS_STDIO)
    
    # Release the Propeller's reset
    setPinDir(5, True)
    writePin(5,True)
        
    # SPI interface
    spiInit(1,1,True,True)    
    
    # For the button input
    setPinDir(PIN_BUTTON,False)
    setPinPullup(PIN_BUTTON,True)
    monitorPin(PIN_BUTTON, True)
    
    # For the chip select output
    setPinDir(PIN_CS,True)
    writePin(PIN_CS,True)   # Active low (idle high)
    
    configureDisplay()

def crossConnectForProgramming():
    
    # Button
    setPinDir(PIN_BUTTON,False)
    setPinPullup(PIN_BUTTON,True)
    
    # Release the Propeller's reset
    setPinDir(5, True)
    writePin(5,True)    
    
    initUart(0, 57600)            # UART0 at 57600
    flowControl(0, False)         # Character mode, no echo  
                   
    ucastSerial("\x00\x00\x20")            # UART0 goes back to controller
    crossConnect(DS_UART0, DS_TRANSPARENT) # Incoming goes to UART0    

def usingPropPlug():
    
    # Button
    setPinDir(PIN_BUTTON,False)
    setPinPullup(PIN_BUTTON,True)
    
    # Let the prop-plug have the pins
    setPinDir(5, False)
    setPinDir(3, False)
    setPinDir(4, False)


@setHook(HOOK_STDIN)
def _stdinput(val):
    pass


@setHook(HOOK_100MS)
def _timerHook100MS(tick):     

    global bootWait
    
    if bootWait>0:
        bootWait = bootWait - 1
        if bootWait == 0:
            configureDisplay()
            p = 1
            p = type(p)
            print p
        return


@setHook(HOOK_GPIN)
def _pinChanged(pin,value):    
    print pin, value


def configureDisplay():
    # 04 - Hide Cursor
    # 14 - Scroll Off (allows writing the bottom/right character)
    # 0C - Clear Display, Cursor to upper left
    sendCodeString('\x04\x14\x0C')
    
def setDisplayMessage(message):
    configureDisplay()
    sendCodeString(message)
    
def _center(line):
    pad = (16-len(line))/2
    while pad>0:
        line = " "+line
        pad = pad - 1
    while len(line)<16:
        line = line + " "  
    return line

def writeTopLine(msg):
    m = '\x11\x00\x00' + msg
    sendCodeString(m)

def writeBottomLine(msg):
    m = '\x11\x00\x01' + msg
    sendCodeString(m)

def centerLines(top,bottom):        
    if top is not None:
        writeTopLine(_center(top))
    if bottom is not None:
        writeBottomLine(_center(bottom))

def sendCodeString(code):
    writePin(PIN_CS,False)  # Enable display SPI
    spiWrite(code)
    writePin(PIN_CS,True)   # Disable display SPI

def startSequenceA(s):
    global sequenceA, seq_posA
    sequenceA = s
    seq_posA = 0
 
def startSequenceB(s):
    global sequenceB, seq_posB
    sequenceB = s
    seq_posB = 0   
    
def stopSequenceA(s):
    global sequenceA, seq_posA
    sequenceA = s
    seq_posA = 0