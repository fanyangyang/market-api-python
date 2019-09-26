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

from market_client.models.store_app import StoreApp  # noqa: F401,E501


class AppListResponse(object):
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
        'list': 'list[StoreApp]',
        'page': 'int',
        'total': 'int'
    }

    attribute_map = {
        'list': 'list',
        'page': 'page',
        'total': 'total'
    }

    def __init__(self, list=None, page=None, total=None):  # noqa: E501
        """AppListResponse - a model defined in Swagger"""  # noqa: E501

        self._list = None
        self._page = None
        self._total = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if page is not None:
            self.page = page
        if total is not None:
            self.total = total

    @property
    def list(self):
        """Gets the list of this AppListResponse.  # noqa: E501


        :return: The list of this AppListResponse.  # noqa: E501
        :rtype: list[StoreApp]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this AppListResponse.


        :param list: The list of this AppListResponse.  # noqa: E501
        :type: list[StoreApp]
        """

        self._list = list

    @property
    def page(self):
        """Gets the page of this AppListResponse.  # noqa: E501


        :return: The page of this AppListResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AppListResponse.


        :param page: The page of this AppListResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def total(self):
        """Gets the total of this AppListResponse.  # noqa: E501


        :return: The total of this AppListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AppListResponse.


        :param total: The total of this AppListResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(AppListResponse, dict):
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
        if not isinstance(other, AppListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
