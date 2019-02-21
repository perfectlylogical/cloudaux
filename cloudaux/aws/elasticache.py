from cloudaux.aws.sts import sts_conn
from cloudaux.exceptions import CloudAuxException
from cloudaux.aws.decorators import rate_limited, paginated

@paginated('CacheClusters')
@sts_conn('elasticache')
@rate_limited()
def describe_cache_clusters(client=None):
    """
    Permission: elasticache:DescribeCacheClusters
    """
    kwargs = dict()
    return client.describe_cache_clusters(**kwargs)
