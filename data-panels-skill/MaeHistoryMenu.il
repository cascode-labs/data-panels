define(axlGetDataViewHistoryUserMenu(axlSessionName historySDB)
  "Adds a menu to run datapanels from Cadence Virtuoso to the Maestro view
  history context (right mouse button) menu.  This overrides a Cadence function
  to customize it"
  let((tests firstTestResultDir)
  tests = maeGetSetup(?typeName "tests"
          ?enabled t
          ?session axlSessionName)
  firstTestResultDir = axlGetPointRunDir(historySDB car(tests))
  if(listp(firstTestResultDir) then
    firstTestResultDir = cadar(firstTestResultDir)  ; get path from (("1st_test_name" "path")...)
  )
  ; Remove the last 2 directories from the path (/psf/[TEST_NAME])
  DP_RESULT_PATH = simplifyFilename(strcat(firstTestResultDir "/../.."))
  DP_RESULT_PATH = substring(DP_RESULT_PATH 1 length(DP_RESULT_PATH)-1) ; Remove trailing slash
  DP_LCVH = list(axlGetSessionLibName(axlSessionName)
                axlGetSessionCellName(axlSessionName)
                axlGetSessionViewName(axlSessionName)
                axlGetHistoryName(historySDB))

  ; Add to menu.
  list(
    list("Results Path" "printf(\"Result directory for %s is at:\n  %s\n\" nth(3 DP_LCVH) DP_RESULT_PATH)" "false")
    list("Run Data-panels Report" "Import['DataPanels]->Run(nth(0 DP_LCVH) nth(1 DP_LCVH) nth(2 DP_LCVH) nth(3 DP_LCVH))" "false")
  )
))
