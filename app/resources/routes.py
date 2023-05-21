from .muvie import MuvieApi, MuviesApi, TestApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
  api.add_resource(MuviesApi, '/api/muvies')
  api.add_resource(MuvieApi, '/api/muvies/<id>')
  api.add_resource(SignupApi, '/api/auth/signup')
  api.add_resource(LoginApi, '/api/auth/login')
  api.add_resource(TestApi, '/api/test')
  api.add_resource(ForgotPassword, '/api/auth/forgot')
  api.add_resource(ResetPassword, '/api/auth/reset')
