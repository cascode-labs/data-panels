; Adds the menu to run datapanels from Cadence Virtuoso

procedure(DpRun(lib cell view history)
  "Run data-panels from the command line"
  let((sessionName resultPath state_view_path command)
  sessionName = maeOpenSetup(lib cell view ?histName history ?mode "r")
  resultPath = EFF_createFromMenu(lib cell view history)
  state_view_path = DpGetStateViewPath()
  if(state_view_path then
    command = strcat("data-panels --dataset " resultPath " --state " state_view_path)
  else
    command = strcat("data-panels --dataset " resultPath)
  )
  ipcBeginProcess(command "" nil nil nil strcat(resultPath "/datapanels-virtuoso.log"))
))

procedure(DpGetStateViewPath(lib cell)
    nil
)

define(axlGetDataViewHistoryUserMenu(axlSessionName historySDB) let((tests firstTestResultDir)
   tests = maeGetSetup(?typeName "tests"
						?enabled t
						?session axlSessionName)
   firstTestResultDir = axlGetPointRunDir(historySDB car(tests))
   if(listp(firstTestResultDir) then
     firstTestResultDir = cadar(firstTestResultDir)  ; get path from (("1st_test_name" "path")...)
   )
   ; Remove the last 2 directories from the path (/psf/[TEST_NAME])
   DP_RESULT_PATH = simplifyFilename(strcat(firstTestResultDir "/../.."))
   DP_RESULT_PATH = substring(DP_resultPath 1 length(DP_resultPath)-1) ; Remove trailing slash
   DP_LCVH = list(axlGetSessionLibName(axlSessionName)
                  axlGetSessionCellName(axlSessionName)
                  axlGetSessionViewName(axlSessionName)
                  axlGetHistoryName(historySDB))

   ; Add to menu.
   list(list("Results Path" "printf(\"Result directory for %s is at:  %s\n\" nth(3 DP_LCVH) DP_RESULT_PATH)" "false")
      ; data-panels is a submenu
      list("data-panels" list(
         ; submenu items
         list("Run" "DpRun(nth(0 DP_LCVH) nth(1 DP_LCVH) nth(2 DP_LCVH) nth(3 DP_LCVH))" "false")
      )
   ))
))
