from aws_cdk import (
    aws_s3 as s3,
    core
)


class TestlibcdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        print("stampo id")
        print(id)

        bucket = s3.Bucket(
            self,
            "testlibcdkbucketzord",
            bucket_name="bucketnamezordz"
        )
