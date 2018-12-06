#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Event
SetKeyDelay 16, 16, 16
#InstallMouseHook
#InstallKeybdHook

;Ctrl&Shift do not allow Delete key to remove modules in VCV Rack

Xbutton1::
Send {BS}
return

esc::exitapp