$lastNumber = QueueTicket::max('queue_number') ?? 0;
$newNumber = $lastNumber + 1;

QueueTicket::create([
    'appointment_id' => $appointment->id,
    'queue_number' => $newNumber,
    'status' => 'waiting',
]);
