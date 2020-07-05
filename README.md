# Rever Python Logger Library

## Install

Add to your requirements.txt

```
git+https://github.com/reverscore/rever-python-loger.git
```

Then install your dependencies

## How to use

To import add:

```
from rever_logger.logger import Logger
log = Logger('service-reports', __name__)
```

Then use all traditional methods to log:

```
log.info
log.error
log.warning
log.debug
log.critical
log.exception
```

## Metadata

To log metadata just pass it as a second argument.

```
log.info('Response is', response)
```

## Exceptions

To properly format exceptions, there's a method that helps by passing a possible exception and formatting it right.

```
except Exception as error:
        log.exception(error)
```
