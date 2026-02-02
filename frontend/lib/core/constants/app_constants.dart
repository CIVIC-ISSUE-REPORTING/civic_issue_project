// Application-wide constants

class AppConstants {
  static const String appName = 'Civic Issue Manager';
  static const String apiBaseUrl = 'https://api.civicissue.com';
  static const int apiTimeout = 30;
  
  // Issue categories
  static const List<String> issueCategories = [
    'Road',
    'Water',
    'Electricity',
    'Sanitation',
    'Parks',
    'Other',
  ];
  
  // Priority levels
  static const List<String> priorityLevels = [
    'Low',
    'Medium',
    'High',
    'Critical',
  ];
}
