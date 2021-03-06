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


class Body1(object):
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
        'details': 'str',
        'group_key': 'str',
        'group_share_alias': 'str',
        'group_template': 'str',
        'group_version': 'str',
        'group_version_alias': 'str',
        'logo': 'str',
        'publish_team': 'str',
        'publish_user': 'str',
        'rainbond_version': 'str',
        'share_type': 'str',
        'template_version': 'str',
        'tenant_id': 'str',
        'update_note': 'str'
    }

    attribute_map = {
        'details': 'details',
        'group_key': 'group_key',
        'group_share_alias': 'group_share_alias',
        'group_template': 'group_template',
        'group_version': 'group_version',
        'group_version_alias': 'group_version_alias',
        'logo': 'logo',
        'publish_team': 'publish_team',
        'publish_user': 'publish_user',
        'rainbond_version': 'rainbond_version',
        'share_type': 'share_type',
        'template_version': 'template_version',
        'tenant_id': 'tenant_id',
        'update_note': 'update_note'
    }

    def __init__(self, details=None, group_key=None, group_share_alias=None, group_template=None, group_version=None, group_version_alias=None, logo=None, publish_team=None, publish_user=None, rainbond_version=None, share_type=None, template_version=None, tenant_id=None, update_note=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._group_key = None
        self._group_share_alias = None
        self._group_template = None
        self._group_version = None
        self._group_version_alias = None
        self._logo = None
        self._publish_team = None
        self._publish_user = None
        self._rainbond_version = None
        self._share_type = None
        self._template_version = None
        self._tenant_id = None
        self._update_note = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if group_key is not None:
            self.group_key = group_key
        if group_share_alias is not None:
            self.group_share_alias = group_share_alias
        if group_template is not None:
            self.group_template = group_template
        if group_version is not None:
            self.group_version = group_version
        if group_version_alias is not None:
            self.group_version_alias = group_version_alias
        if logo is not None:
            self.logo = logo
        if publish_team is not None:
            self.publish_team = publish_team
        if publish_user is not None:
            self.publish_user = publish_user
        if rainbond_version is not None:
            self.rainbond_version = rainbond_version
        if share_type is not None:
            self.share_type = share_type
        if template_version is not None:
            self.template_version = template_version
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if update_note is not None:
            self.update_note = update_note

    @property
    def details(self):
        """Gets the details of this Body1.  # noqa: E501


        :return: The details of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Body1.


        :param details: The details of this Body1.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def group_key(self):
        """Gets the group_key of this Body1.  # noqa: E501


        :return: The group_key of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._group_key

    @group_key.setter
    def group_key(self, group_key):
        """Sets the group_key of this Body1.


        :param group_key: The group_key of this Body1.  # noqa: E501
        :type: str
        """

        self._group_key = group_key

    @property
    def group_share_alias(self):
        """Gets the group_share_alias of this Body1.  # noqa: E501


        :return: The group_share_alias of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._group_share_alias

    @group_share_alias.setter
    def group_share_alias(self, group_share_alias):
        """Sets the group_share_alias of this Body1.


        :param group_share_alias: The group_share_alias of this Body1.  # noqa: E501
        :type: str
        """

        self._group_share_alias = group_share_alias

    @property
    def group_template(self):
        """Gets the group_template of this Body1.  # noqa: E501


        :return: The group_template of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._group_template

    @group_template.setter
    def group_template(self, group_template):
        """Sets the group_template of this Body1.


        :param group_template: The group_template of this Body1.  # noqa: E501
        :type: str
        """

        self._group_template = group_template

    @property
    def group_version(self):
        """Gets the group_version of this Body1.  # noqa: E501


        :return: The group_version of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """Sets the group_version of this Body1.


        :param group_version: The group_version of this Body1.  # noqa: E501
        :type: str
        """

        self._group_version = group_version

    @property
    def group_version_alias(self):
        """Gets the group_version_alias of this Body1.  # noqa: E501


        :return: The group_version_alias of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._group_version_alias

    @group_version_alias.setter
    def group_version_alias(self, group_version_alias):
        """Sets the group_version_alias of this Body1.


        :param group_version_alias: The group_version_alias of this Body1.  # noqa: E501
        :type: str
        """

        self._group_version_alias = group_version_alias

    @property
    def logo(self):
        """Gets the logo of this Body1.  # noqa: E501


        :return: The logo of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Body1.


        :param logo: The logo of this Body1.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def publish_team(self):
        """Gets the publish_team of this Body1.  # noqa: E501


        :return: The publish_team of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._publish_team

    @publish_team.setter
    def publish_team(self, publish_team):
        """Sets the publish_team of this Body1.


        :param publish_team: The publish_team of this Body1.  # noqa: E501
        :type: str
        """

        self._publish_team = publish_team

    @property
    def publish_user(self):
        """Gets the publish_user of this Body1.  # noqa: E501


        :return: The publish_user of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._publish_user

    @publish_user.setter
    def publish_user(self, publish_user):
        """Sets the publish_user of this Body1.


        :param publish_user: The publish_user of this Body1.  # noqa: E501
        :type: str
        """

        self._publish_user = publish_user

    @property
    def rainbond_version(self):
        """Gets the rainbond_version of this Body1.  # noqa: E501


        :return: The rainbond_version of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._rainbond_version

    @rainbond_version.setter
    def rainbond_version(self, rainbond_version):
        """Sets the rainbond_version of this Body1.


        :param rainbond_version: The rainbond_version of this Body1.  # noqa: E501
        :type: str
        """

        self._rainbond_version = rainbond_version

    @property
    def share_type(self):
        """Gets the share_type of this Body1.  # noqa: E501


        :return: The share_type of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this Body1.


        :param share_type: The share_type of this Body1.  # noqa: E501
        :type: str
        """

        self._share_type = share_type

    @property
    def template_version(self):
        """Gets the template_version of this Body1.  # noqa: E501


        :return: The template_version of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._template_version

    @template_version.setter
    def template_version(self, template_version):
        """Sets the template_version of this Body1.


        :param template_version: The template_version of this Body1.  # noqa: E501
        :type: str
        """

        self._template_version = template_version

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Body1.  # noqa: E501


        :return: The tenant_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Body1.


        :param tenant_id: The tenant_id of this Body1.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def update_note(self):
        """Gets the update_note of this Body1.  # noqa: E501


        :return: The update_note of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._update_note

    @update_note.setter
    def update_note(self, update_note):
        """Sets the update_note of this Body1.


        :param update_note: The update_note of this Body1.  # noqa: E501
        :type: str
        """

        self._update_note = update_note

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
