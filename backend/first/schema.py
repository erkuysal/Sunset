import strawberry
from django.contrib.auth.hashers import make_password
from gqlauth.user.queries import UserQueries, UserType
from django.contrib.auth import get_user_model
from gqlauth.core.middlewares import JwtSchema

from gqlauth.user import arg_mutations as mutations


@strawberry.type
class Query(UserQueries):
    # you can add your queries here
    ...


@strawberry.django.type(model=get_user_model())
class MyQueries:
    me: UserType = UserQueries.me
    public: UserType = UserQueries.public_user
    # etc...


@strawberry.type
class Mutation:

    # include what-ever mutations you want.
    verify_token = mutations.VerifyToken.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field
    token_auth = mutations.ObtainJSONWebToken.field

    update_account = mutations.UpdateAccount.field
    verify_account = mutations.VerifyAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field

    password_set = mutations.PasswordSet.field
    password_change = mutations.PasswordChange.field
    password_reset = mutations.PasswordReset.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    resend_activation_email = mutations.ResendActivationEmail.field
    # verify_secondary_email = mutations.VerifySecondaryEmail.field
    # swap_emails = mutations.SwapEmails.field

    # captcha = Captcha.field

    register = mutations.Register.field

# This is essentially the same as strawberries schema though it
# injects the user to `info.context["request"].user`


schema = JwtSchema(query=Query, mutation=Mutation)
