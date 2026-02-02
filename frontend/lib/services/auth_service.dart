class AuthService {
  String? _token;
  String? _userId;
  
  Future<bool> login(String email, String password) async {
    // TODO: Implement login logic
    // Call API, store token
    return true;
  }
  
  Future<void> logout() async {
    _token = null;
    _userId = null;
  }
  
  bool isAuthenticated() {
    return _token != null;
  }
  
  String? getToken() {
    return _token;
  }
  
  String? getUserId() {
    return _userId;
  }
}
