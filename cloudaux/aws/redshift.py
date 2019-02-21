from cloudaux.aws.sts import sts_conn
from cloudaux.exceptions import CloudAuxException
from cloudaux.aws.decorators import rate_limited, paginated

@paginated('Clusters')
@sts_conn('redshift')
@rate_limited()
def describe_clusters(client=None):
    """
    Permission: redshift:DescribeClusters
    """
    kwargs = dict()
    return client.describe_clusters(**kwargs)
