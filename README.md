# QGIS_IoT_plugin
QGIS에서 외부의 IoT 센서에서 UDP로 전달되는 값을 처리하는 플러그인


## deploy
src 폴더의 pb_tool_example.cfg 파일을 pb_tool.cfg 로 변경해서 사용해야 한다.

만약 `pb_tool deploy` 했을 때 빌드한 플러그인을 어디에 복사해 넣어야 할지 모르겠다고, 너의 QGIS 플러그인 폴더가 어디인지 모르겠다는 메시지가 나오면 pb_tool.cfg 파일을 열어 plugin_path 부분을 수정해 주면 된다. QGIS 3에서는 다음과 같은 식이다.

```
plugin_path:C:\Users\<윈도우 아이디>\AppData\Roaming\QGIS\QGIS3\profiles\<QGIS 프로필 아이디>\python\plugins
```

## vscode에서 코드 자동 완성

qgis 3.44.7 기준

프로젝트 폴더에 `.env` 파일을 만든다. 
그 파일의 내용으로 

```
PYTHONPATH=C:/Program Files/QGIS 3.44.7/apps/qgis/python;C:/Program Files/QGIS 3.44.7/apps/Python312/Lib/site-packages
```

을 한 줄로 입력한다. 

버전이 바뀌면 QGIS 버전과 python 버전을 확인해야 한다. 

이제 vscode를 (다시) 실행한다. 

프로그램 실행은 안 되도 code intellisense는 잘 된다.

vs code에서 아래 코드를 실행해 보자. 

```
import qgis.core

print(qgis.core.QgsApplication.showSettings())
``