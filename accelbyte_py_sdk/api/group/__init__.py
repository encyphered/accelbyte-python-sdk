"""Auto-generated top-level package for the group API."""

__version__ = "2.4.0"
__author__ = "AccelByte"
__email__ = "dev@accelbyte.net"

# configuration
from .wrappers import list_group_configuration_admin_v1
from .wrappers import create_group_configuration_admin_v1
from .wrappers import initiate_group_configuration_admin_v1
from .wrappers import get_group_configuration_admin_v1
from .wrappers import delete_group_configuration_admin_v1
from .wrappers import update_group_configuration_admin_v1
from .wrappers import update_group_configuration_global_rule_admin_v1
from .wrappers import delete_group_configuration_global_rule_admin_v1

# group
from .wrappers import get_group_list_admin_v1
from .wrappers import get_single_group_admin_v1
from .wrappers import delete_group_admin_v1
from .wrappers import get_group_list_public_v1
from .wrappers import create_new_group_public_v1
from .wrappers import get_single_group_public_v1
from .wrappers import update_single_group_public_v1
from .wrappers import delete_group_public_v1
from .wrappers import update_single_group_partial_public_v1
from .wrappers import update_group_custom_attributes_public_v1
from .wrappers import update_group_custom_rule_public_v1
from .wrappers import update_group_predefined_rule_public_v1
from .wrappers import delete_group_predefined_rule_public_v1

# group_member
from .wrappers import get_group_members_list_v1
from .wrappers import accept_group_invitation_public_v1
from .wrappers import reject_group_invitation_public_v1
from .wrappers import join_group_v1
from .wrappers import cancel_group_join_request_v1
from .wrappers import get_group_members_list_public_v1
from .wrappers import leave_group_public_v1
from .wrappers import get_user_group_information_public_v1
from .wrappers import invite_group_public_v1
from .wrappers import accept_group_join_request_public_v1
from .wrappers import reject_group_join_request_public_v1
from .wrappers import kick_group_member_public_v1

# group_roles
from .wrappers import get_member_roles_list_admin_v1
from .wrappers import create_member_role_admin_v1
from .wrappers import get_single_member_role_admin_v1
from .wrappers import delete_member_role_admin_v1
from .wrappers import update_member_role_admin_v1
from .wrappers import update_member_role_permission_admin_v1
from .wrappers import get_member_roles_list_public_v1
from .wrappers import assign_role_to_group_member_admin_v1
from .wrappers import delete_member_role_public_v1

# member_request
from .wrappers import get_group_join_request_public_v1
from .wrappers import get_group_invitation_request_public_v1
