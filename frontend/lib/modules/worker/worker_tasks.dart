import 'package:flutter/material.dart';

class WorkerTasks extends StatelessWidget {
  const WorkerTasks({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('My Tasks'),
      ),
      body: ListView.builder(
        itemCount: 10,
        itemBuilder: (context, index) {
          return ListTile(
            leading: const CircleAvatar(child: Icon(Icons.work)),
            title: Text('Task #${index + 1}'),
            subtitle: const Text('Description of the assigned task'),
            trailing: const Icon(Icons.arrow_forward_ios),
            onTap: () {},
          );
        },
      ),
    );
  }
}
