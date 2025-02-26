# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KafkaCredentialArgs', 'KafkaCredential']

@pulumi.input_type
class KafkaCredentialArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 credential_name: pulumi.Input[str],
                 permissions: pulumi.Input[str],
                 topic: pulumi.Input[str]):
        """
        The set of arguments for constructing a KafkaCredential resource.
        :param pulumi.Input[str] cluster_id: ID of the kafka cluster
        :param pulumi.Input[str] credential_name: Name of the kafka credential
        :param pulumi.Input[str] permissions: Permission scope given to the kafka credential
        :param pulumi.Input[str] topic: Name of the kafka topic
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "credential_name", credential_name)
        pulumi.set(__self__, "permissions", permissions)
        pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        ID of the kafka cluster
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> pulumi.Input[str]:
        """
        Name of the kafka credential
        """
        return pulumi.get(self, "credential_name")

    @credential_name.setter
    def credential_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "credential_name", value)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[str]:
        """
        Permission scope given to the kafka credential
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[str]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Input[str]:
        """
        Name of the kafka topic
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic", value)


@pulumi.input_type
class _KafkaCredentialState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 credential_id: Optional[pulumi.Input[str]] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KafkaCredential resources.
        :param pulumi.Input[str] cluster_id: ID of the kafka cluster
        :param pulumi.Input[int] creation_time: Creation time of the credential
        :param pulumi.Input[str] credential_id: Unique ID of the kafka credential
        :param pulumi.Input[str] credential_name: Name of the kafka credential
        :param pulumi.Input[str] password: Password to be used in authenticating to the cluster
        :param pulumi.Input[str] permissions: Permission scope given to the kafka credential
        :param pulumi.Input[str] state: State of the credential(active or deleted)
        :param pulumi.Input[str] topic: Name of the kafka topic
        :param pulumi.Input[str] username: Username to be used for the kafka credential
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if credential_id is not None:
            pulumi.set(__self__, "credential_id", credential_id)
        if credential_name is not None:
            pulumi.set(__self__, "credential_name", credential_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the kafka cluster
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        """
        Creation time of the credential
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique ID of the kafka credential
        """
        return pulumi.get(self, "credential_id")

    @credential_id.setter
    def credential_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_id", value)

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the kafka credential
        """
        return pulumi.get(self, "credential_name")

    @credential_name.setter
    def credential_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password to be used in authenticating to the cluster
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[str]]:
        """
        Permission scope given to the kafka credential
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the credential(active or deleted)
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the kafka topic
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username to be used for the kafka credential
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class KafkaCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import upstash_pulumi as upstash

        example_kafka_cluster = upstash.KafkaCluster("exampleKafkaCluster",
            cluster_name=var["cluster_name"],
            region=var["region"],
            multizone=var["multizone"])
        example_kafka_topic = upstash.KafkaTopic("exampleKafkaTopic",
            topic_name=var["topic_name"],
            partitions=var["partitions"],
            retention_time=var["retention_time"],
            retention_size=var["retention_size"],
            max_message_size=var["max_message_size"],
            cleanup_policy=var["cleanup_policy"],
            cluster_id=resource["upstash_kafka_cluster"]["exampleKafkaCluster"]["cluster_id"])
        example_kafka_credential = upstash.KafkaCredential("exampleKafkaCredential",
            cluster_id=example_kafka_cluster.cluster_id,
            credential_name="credentialFromTerraform",
            topic=example_kafka_topic.topic_name,
            permissions="ALL")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: ID of the kafka cluster
        :param pulumi.Input[str] credential_name: Name of the kafka credential
        :param pulumi.Input[str] permissions: Permission scope given to the kafka credential
        :param pulumi.Input[str] topic: Name of the kafka topic
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KafkaCredentialArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import upstash_pulumi as upstash

        example_kafka_cluster = upstash.KafkaCluster("exampleKafkaCluster",
            cluster_name=var["cluster_name"],
            region=var["region"],
            multizone=var["multizone"])
        example_kafka_topic = upstash.KafkaTopic("exampleKafkaTopic",
            topic_name=var["topic_name"],
            partitions=var["partitions"],
            retention_time=var["retention_time"],
            retention_size=var["retention_size"],
            max_message_size=var["max_message_size"],
            cleanup_policy=var["cleanup_policy"],
            cluster_id=resource["upstash_kafka_cluster"]["exampleKafkaCluster"]["cluster_id"])
        example_kafka_credential = upstash.KafkaCredential("exampleKafkaCredential",
            cluster_id=example_kafka_cluster.cluster_id,
            credential_name="credentialFromTerraform",
            topic=example_kafka_topic.topic_name,
            permissions="ALL")
        ```

        :param str resource_name: The name of the resource.
        :param KafkaCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KafkaCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KafkaCredentialArgs.__new__(KafkaCredentialArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if credential_name is None and not opts.urn:
                raise TypeError("Missing required property 'credential_name'")
            __props__.__dict__["credential_name"] = credential_name
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
            if topic is None and not opts.urn:
                raise TypeError("Missing required property 'topic'")
            __props__.__dict__["topic"] = topic
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["credential_id"] = None
            __props__.__dict__["password"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["username"] = None
        super(KafkaCredential, __self__).__init__(
            'upstash:index/kafkaCredential:KafkaCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            credential_id: Optional[pulumi.Input[str]] = None,
            credential_name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            topic: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'KafkaCredential':
        """
        Get an existing KafkaCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: ID of the kafka cluster
        :param pulumi.Input[int] creation_time: Creation time of the credential
        :param pulumi.Input[str] credential_id: Unique ID of the kafka credential
        :param pulumi.Input[str] credential_name: Name of the kafka credential
        :param pulumi.Input[str] password: Password to be used in authenticating to the cluster
        :param pulumi.Input[str] permissions: Permission scope given to the kafka credential
        :param pulumi.Input[str] state: State of the credential(active or deleted)
        :param pulumi.Input[str] topic: Name of the kafka topic
        :param pulumi.Input[str] username: Username to be used for the kafka credential
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KafkaCredentialState.__new__(_KafkaCredentialState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["credential_id"] = credential_id
        __props__.__dict__["credential_name"] = credential_name
        __props__.__dict__["password"] = password
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["state"] = state
        __props__.__dict__["topic"] = topic
        __props__.__dict__["username"] = username
        return KafkaCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        ID of the kafka cluster
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        Creation time of the credential
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> pulumi.Output[str]:
        """
        Unique ID of the kafka credential
        """
        return pulumi.get(self, "credential_id")

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> pulumi.Output[str]:
        """
        Name of the kafka credential
        """
        return pulumi.get(self, "credential_name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Password to be used in authenticating to the cluster
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[str]:
        """
        Permission scope given to the kafka credential
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the credential(active or deleted)
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        Name of the kafka topic
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Username to be used for the kafka credential
        """
        return pulumi.get(self, "username")

