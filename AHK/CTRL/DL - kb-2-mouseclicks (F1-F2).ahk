#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
; Recommended for performance
#NoEnv

; Better and more reliable
SendMode Input

; Press the right mouse button unless it's already pressed.
F2::
 if ( not GetKeyState("RButton" , "P") )
  Click down right
return

; Release the mouse button when the key is released.
F2 Up::Click up right

F1::
 if ( not GetKeyState("LButton" , "P") )
  Click down
return

F1 Up::Click up
