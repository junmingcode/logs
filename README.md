# logs
基于logging模块，设置日志输出位置，日志文件大小等。方便使用
使用方法，引入模块
from logs import Logger
logger = Logger()
下面是必须的赋值操作，或者直接使用方法也是可以的
logger.debug=logger._debug()
logger.info=logger._info()
logger.warning=logger._warning()
logger.error=logger._error()
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")

直接使用：
logger._debug()("debug")
logger._info()("info")
logger._warning()("warning")
logger._error()("error")
