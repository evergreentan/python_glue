clear all
set more off

local y `1'
local x1 `2'
local x2 `3'

display `"first parameter: `y'"'
display `"second parameter: `x1'"'
display `"third parameter: `x2'"'

sysuse auto
regress `y' `x1' `x2'

//exit, STATA clear
