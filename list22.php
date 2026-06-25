public function complete(Appointment $appointment)
{
    $appointment->update([
        'status' => 'completed',
    ]);

    if ($appointment->queueTicket) {
        $appointment->queueTicket->update([
            'status' => 'completed',
        ]);
    }

    return back()->with('success', 'Обслуживание завершено.');
}
