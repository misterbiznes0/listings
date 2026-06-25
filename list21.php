public function call(Appointment $appointment)
{
    $appointment->update([
        'status' => 'called',
    ]);

    if ($appointment->queueTicket) {
        $appointment->queueTicket->update([
            'status' => 'called',
        ]);
    }

    return back()->with('success', 'Посетитель вызван.');
}
