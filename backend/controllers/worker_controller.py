class WorkerController:
    def get_worker_tasks(self, worker_id):
        # TODO: Fetch tasks assigned to worker
        return []
    
    def accept_task(self, task_id, worker_id):
        # TODO: Update task status to accepted
        return {
            'message': 'Task accepted',
            'task_id': task_id
        }
    
    def complete_task(self, task_id, worker_id, data):
        # TODO: Verify completion with ML model
        # Update task status to completed
        return {
            'message': 'Task completed',
            'task_id': task_id
        }
    
    def update_task_status(self, task_id, data):
        # TODO: Update task status
        return {
            'message': 'Task status updated',
            'task_id': task_id,
            'status': data.get('status')
        }
