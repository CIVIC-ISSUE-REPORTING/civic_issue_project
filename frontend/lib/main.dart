import 'package:flutter/material.dart';

void main() {
  runApp(const CivicIssueApp());
}

class CivicIssueApp extends StatelessWidget {
  const CivicIssueApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Civic Issue Manager',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Civic Issue Manager'),
      ),
      body: const Center(
        child: Text('Welcome to Civic Issue Management System'),
      ),
    );
  }
}
