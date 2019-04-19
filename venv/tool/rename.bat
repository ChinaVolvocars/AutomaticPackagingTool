@echo off&&setlocal enabledelayedexpansion

for %%i in (*.apk) do (

set ym=%%i

set ym=!ym:_4.0.9_official_5744605b_enc_zipalign_=-!

if %%i neq !ym! (ren "%%i" "!ym!")

)

endlocal 