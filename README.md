# QGIS_IoT_plugin
QGIS에서 외부의 IoT 센서에서 UDP로 전달되는 값을 처리하는 플러그인

src 폴더의 pb_tool_example.cfg 파일을 pb_tool.cfg 로 변경해서 사용해야 한다.

만약 `pb_tool deploy` 했을 때 빌드한 플러그인을 어디에 복사해 넣어야 할지 모르겠다고, 너의 QGIS 플러그인 폴더가 어디인지 모르겠다는 메시지가 나오면 pb_tool.cfg 파일을 열어 plugin_path 부분을 수정해 주면 된다. QGIS 3에서는 다음과 같은 식이다.

```
plugin_path:C:\Users\<윈도우 아이디>\AppData\Roaming\QGIS\QGIS3\profiles\<QGIS 프로필 아이디>\python\plugins
```