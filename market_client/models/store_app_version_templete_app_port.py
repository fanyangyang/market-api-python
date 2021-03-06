# coding: utf-8

"""
    rainbond cloud app market OpenAPI.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: 576501057@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StoreAppVersionTempleteAppPort(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'container_port': 'int',
        'is_inner_service': 'bool',
        'is_outer_service': 'bool',
        'port_alias': 'str',
        'protocol': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'container_port': 'container_port',
        'is_inner_service': 'is_inner_service',
        'is_outer_service': 'is_outer_service',
        'port_alias': 'port_alias',
        'protocol': 'protocol',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, container_port=None, is_inner_service=None, is_outer_service=None, port_alias=None, protocol=None, tenant_id=None):  # noqa: E501
        """StoreAppVersionTempleteAppPort - a model defined in Swagger"""  # noqa: E501

        self._container_port = None
        self._is_inner_service = None
        self._is_outer_service = None
        self._port_alias = None
        self._protocol = None
        self._tenant_id = None
        self.discriminator = None

        if container_port is not None:
            self.container_port = container_port
        if is_inner_service is not None:
            self.is_inner_service = is_inner_service
        if is_outer_service is not None:
            self.is_outer_service = is_outer_service
        if port_alias is not None:
            self.port_alias = port_alias
        if protocol is not None:
            self.protocol = protocol
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def container_port(self):
        """Gets the container_port of this StoreAppVersionTempleteAppPort.  # noqa: E501


        :return: The container_port of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        """Sets the container_port of this StoreAppVersionTempleteAppPort.


        :param container_port: The container_port of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :type: int
        """

        self._container_port = container_port

    @property
    def is_inner_service(self):
        """Gets the is_inner_service of this StoreAppVersionTempleteAppPort.  # noqa: E501


        :return: The is_inner_service of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :rtype: bool
        """
        return self._is_inner_service

    @is_inner_service.setter
    def is_inner_service(self, is_inner_service):
        """Sets the is_inner_service of this StoreAppVersionTempleteAppPort.


        :param is_inner_service: The is_inner_service of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :type: bool
        """

        self._is_inner_service = is_inner_service

    @property
    def is_outer_service(self):
        """Gets the is_outer_service of this StoreAppVersionTempleteAppPort.  # noqa: E501


        :return: The is_outer_service of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :rtype: bool
        """
        return self._is_outer_service

    @is_outer_service.setter
    def is_outer_service(self, is_outer_service):
        """Sets the is_outer_service of this StoreAppVersionTempleteAppPort.


        :param is_outer_service: The is_outer_service of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :type: bool
        """

        self._is_outer_service = is_outer_service

    @property
    def port_alias(self):
        """Gets the port_alias of this StoreAppVersionTempleteAppPort.  # noqa: E501


        :return: The port_alias of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :rtype: str
        """
        return self._port_alias

    @port_alias.setter
    def port_alias(self, port_alias):
        """Sets the port_alias of this StoreAppVersionTempleteAppPort.


        :param port_alias: The port_alias of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :type: str
        """

        self._port_alias = port_alias

    @property
    def protocol(self):
        """Gets the protocol of this StoreAppVersionTempleteAppPort.  # noqa: E501


        :return: The protocol of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this StoreAppVersionTempleteAppPort.


        :param protocol: The protocol of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def tenant_id(self):
        """Gets the tenant_id of this StoreAppVersionTempleteAppPort.  # noqa: E501


        :return: The tenant_id of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this StoreAppVersionTempleteAppPort.


        :param tenant_id: The tenant_id of this StoreAppVersionTempleteAppPort.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StoreAppVersionTempleteAppPort, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoreAppVersionTempleteAppPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
