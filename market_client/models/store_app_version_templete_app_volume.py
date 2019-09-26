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

from market_client.models.volume_type import VolumeType  # noqa: F401,E501


class StoreAppVersionTempleteAppVolume(object):
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
        'file_content': 'str',
        'volume_name': 'str',
        'volume_path': 'str',
        'volume_type': 'VolumeType'
    }

    attribute_map = {
        'file_content': 'file_content',
        'volume_name': 'volume_name',
        'volume_path': 'volume_path',
        'volume_type': 'volume_type'
    }

    def __init__(self, file_content=None, volume_name=None, volume_path=None, volume_type=None):  # noqa: E501
        """StoreAppVersionTempleteAppVolume - a model defined in Swagger"""  # noqa: E501

        self._file_content = None
        self._volume_name = None
        self._volume_path = None
        self._volume_type = None
        self.discriminator = None

        if file_content is not None:
            self.file_content = file_content
        if volume_name is not None:
            self.volume_name = volume_name
        if volume_path is not None:
            self.volume_path = volume_path
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def file_content(self):
        """Gets the file_content of this StoreAppVersionTempleteAppVolume.  # noqa: E501

        用于配置文件，存储配置文件数据  # noqa: E501

        :return: The file_content of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        """Sets the file_content of this StoreAppVersionTempleteAppVolume.

        用于配置文件，存储配置文件数据  # noqa: E501

        :param file_content: The file_content of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :type: str
        """

        self._file_content = file_content

    @property
    def volume_name(self):
        """Gets the volume_name of this StoreAppVersionTempleteAppVolume.  # noqa: E501


        :return: The volume_name of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this StoreAppVersionTempleteAppVolume.


        :param volume_name: The volume_name of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def volume_path(self):
        """Gets the volume_path of this StoreAppVersionTempleteAppVolume.  # noqa: E501


        :return: The volume_path of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :rtype: str
        """
        return self._volume_path

    @volume_path.setter
    def volume_path(self, volume_path):
        """Sets the volume_path of this StoreAppVersionTempleteAppVolume.


        :param volume_path: The volume_path of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :type: str
        """

        self._volume_path = volume_path

    @property
    def volume_type(self):
        """Gets the volume_type of this StoreAppVersionTempleteAppVolume.  # noqa: E501


        :return: The volume_type of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :rtype: VolumeType
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this StoreAppVersionTempleteAppVolume.


        :param volume_type: The volume_type of this StoreAppVersionTempleteAppVolume.  # noqa: E501
        :type: VolumeType
        """

        self._volume_type = volume_type

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
        if issubclass(StoreAppVersionTempleteAppVolume, dict):
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
        if not isinstance(other, StoreAppVersionTempleteAppVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
