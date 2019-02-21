from cloudaux.aws.sts import sts_conn
from cloudaux.exceptions import CloudAuxException
from cloudaux.aws.decorators import rate_limited, paginated

@paginated('DBInstances')
@sts_conn('rds')
@rate_limited()
def describe_db_instances(client=None):
    """
    Permission: elasticloadbalancing:DescribeLoadBalancers
    """
    kwargs = dict()
    return client.describe_db_instances(**kwargs)
