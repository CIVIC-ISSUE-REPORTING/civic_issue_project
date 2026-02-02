import 'package:flutter/material.dart';

class CitizenHomePage extends StatelessWidget {
  const CitizenHomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Citizen Portal'),
      ),
      body: GridView.count(
        crossAxisCount: 2,
        padding: const EdgeInsets.all(16),
        children: [
          _buildActionCard('Report Issue', Icons.add_circle),
          _buildActionCard('My Issues', Icons.list),
          _buildActionCard('Track Status', Icons.track_changes),
          _buildActionCard('History', Icons.history),
        ],
      ),
    );
  }

  Widget _buildActionCard(String title, IconData icon) {
    return Card(
      child: InkWell(
        onTap: () {},
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 48),
            const SizedBox(height: 8),
            Text(title),
          ],
        ),
      ),
    );
  }
}
