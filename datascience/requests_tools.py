import logging

log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)


def debug_requests(request):
    log.debug(request)
