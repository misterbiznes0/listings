public function update(Request $request, User $user)
{
    $request->validate([
        'name' => 'required|string|max:255',
        'email' => 'required|email|max:255',
        'is_admin' => 'nullable|boolean',
    ]);

    $user->update([
        'name' => $request->name,
        'email' => $request->email,
        'is_admin' => $request->has('is_admin'),
    ]);

    return redirect()
        ->route('admin.users')
        ->with('success', 'Данные пользователя обновлены.');
}
