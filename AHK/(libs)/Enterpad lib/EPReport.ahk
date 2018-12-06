;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
;
; File Name: EPReport.ahk
; WinXP and up
; Tested with AutoHotkey v1.1.09.02
;
; Author: Denis Lamarre, Cedeq
;
; Aug 29, 2018: Added support for more than 999 scripts
; Mar 31, 2017: Progress bar removed
; Feb 12, 2016: Progress bar content modified
; Dec 04, 2015: Commented out the warning if the Enterpad is not present at start
; May 12, 2014: Commented out Dll and Enterpad missing messages if epAllowScriptWithoutEnterpad
; Apr 22, 2014: "epAllowScriptWithoutEnterpad := true" allows the script without the enterpad
; Mar 05, 2014: Border of the progress bar removed
; Feb 16, 2014: Progress bar added
; Jan 12, 2014: Better Sleep/Resume management
;
;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
;
; This software is provided “as is” by the author. No warranties,
; whether express, implied or statutory, including, but not limited
; to, implied warranties of merchantability and fitness for a
; particular purpose apply to this software. The author shall not,
; in any circumstances, be liable for special, incidental or
; consequential damages, for any reason whatsoever.
;
;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Persistent
OnExit, ExitSub

epEnterpadLinkedToThisScript := false
epSessionNotificationRegistred := false
epCountEnterpadPeek = 0
epCountLock   = 0
epCountUnLock = 0
epHandleDllEnterpad = 0
epScriptName := SubStr(A_ScriptName, 1, -4)

epDllIsMissing := "The file 'Enterpad.dll' is probably missing! "
epEnterpadIsMissing := "Enterpad not found! "
epEnterpadCantBeLinked := "The Enterpad can't be linked."
epEnterpadLinkBroken := "Whoops! The Enterpad link has been broken. "
epScriptWillTerminate := "This AutoHotkey script will exit."
epScriptWillContinue := "This AutoHotkey script can be used without the Enterpad"

OnMessage(0x0218, "POWERBROADCAST")

if A_OSVersion not in WIN_2003,WIN_XP,WIN_2000
{
  epHW_ahk := DllCall("FindWindowEx", "uint", 0, "uint", 0, "str", "AutoHotkey", "str", a_ScriptFullPath " - AutoHotkey v" a_AhkVersion )
  OnMessage( 0x02B1, "Handle_WTSSESSION_CHANGE" )
  epSessionNotificationRegistred := DllCall( "wtsapi32.dll\WTSRegisterSessionNotification", "uint", epHW_ahk, "uint", 0x0 )
}

if (!epPathDllEnterpad){
  epPathDllEnterpad := A_ScriptDir . "\Enterpad.dll"
}
epHandleDllEnterpad := DllCall("LoadLibrary", "str", epPathDllEnterpad)

if (!epHandleDllEnterpad){
  if (epAllowScriptWithoutEnterpad){
    ;MsgBox % epDllIsMissing epEnterpadCantBeLinked
    CloseEnterpadLink()
    Return
  }
  else{
    MsgBox % epDllIsMissing epScriptWillTerminate
    ExitApp
  }
}

If ( DllCall(epPathDllEnterpad . "\ReadStatus", "Cdecl Int") != 3 ){
  if (epAllowScriptWithoutEnterpad){
    ;MsgBox % epEnterpadIsMissing epEnterpadCantBeLinked
    CloseEnterpadLink()
    Return
  }
  else{
    ;MsgBox % epEnterpadIsMissing epScriptWillTerminate
    ExitApp
  }
}

epResult := DllCall(epPathDllEnterpad . "\ResetEnterpad", "Cdecl Int")
epEnterpadLinkedToThisScript := true

SetTimer Enterpad_peek, 250

return

;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

POWERBROADCAST(wParam, lParam, msg, hwnd){ 

  Global epEnterpadLinkedToThisScript
  Global epHandleDllEnterpad
 
  If (epHandleDllEnterpad AND epEnterpadLinkedToThisScript){
    If (wParam = 0x04){
      SetTimer Enterpad_peek, Off
    }
    Else If (wParam = 0x12){
      SetTimer Enterpad_peek, On
    }
  }
  ;
  ;
  ;If needed, add custom "Power Notifications" code here
  ;
  ;

  Return True ;True is needed

}

Handle_WTSSESSION_CHANGE( epW, epL, epM, epHW ){

  Global epCountLock
  Global epCountUnLock
  Global epEnterpadLinkedToThisScript
  Global epPathDllEnterpad
  Global epHandleDllEnterpad

  if (epHandleDllEnterpad){
    if ( epW = 0x2 OR epW = 0x7)
    {
      SetTimer Enterpad_peek, Off
      epResult := DllCall(epPathDllEnterpad . "\ResetEnterpad", "Cdecl Int")
      epResult := DllCall(epPathDllEnterpad . "\ReleaseEnterpad", "Cdecl Int")
      epEnterpadLinkedToThisScript := false
      epCountLock++
    }
    Else If ( epW = 0x1 OR epW = 0x8)
    {
      epResult := DllCall(epPathDllEnterpad . "\FindEnterpad", "Cdecl Int")
      epResult := DllCall(epPathDllEnterpad . "\ResetEnterpad", "Cdecl Int")
      SetTimer Enterpad_peek, On
      epEnterpadLinkedToThisScript := true
      epCountUnLock++
    }
  }

  ;
  ;
  ;If needed, add custom "Session Notifications" code here (Vista and up only)
  ;
  ;

}

CloseEnterpadLink(){

  Global epHandleDllEnterpad
  Global epEnterpadLinkedToThisScript

  SetTimer Enterpad_peek, Off

  if (epHandleDllEnterpad){
    epResult := DllCall("FreeLibrary", "UInt", epHandleDllEnterpad)
    epHandleDllEnterpad := 0
  }

  epEnterpadLinkedToThisScript := false

}

;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ExitSub:

  CloseEnterpadLink()

  if (epSessionNotificationRegistred){
    epResult := DllCall("Wtsapi32.dll\WTSUnRegisterSessionNotification", "uint", epHW_ahk)
  }

  ;
  ;
  ;If needed, add custom cleanup code here
  ;
  ;

  ExitApp

;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Enterpad_peek:

  epCountEnterpadPeek++
  epReport_Enterpad := DllCall(epPathDllEnterpad . "\ReadReportInt", "Cdecl Int")
  if (epReport_Enterpad = -1){
    if (epAllowScriptWithoutEnterpad){
      MsgBox % epEnterpadLinkBroken epScriptWillContinue
      CloseEnterpadLink()
      Return
    }
    else{
      MsgBox % epEnterpadLinkBroken epScriptWillTerminate
      ExitApp
    }
  }

  if (epReport_Enterpad < 1000){
    epReport_Enterpad := "00" epReport_Enterpad
    StringRight epReport_Enterpad, epReport_Enterpad, 3
  }
  if IsLabel(epReport_Enterpad){
    epKeys = %epKeys% %epReport_Enterpad%
    StringRight epKeys, epKeys, 28
    epKeyCount++
    SplashImage,,ZH0 B1 y60 CW808080 CTFFFFFF,%epScriptName% %epReport_Enterpad% in process
    gosub %epReport_Enterpad%
    Sleep, 200
    SplashImage, Off
  }
  
  return

;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
