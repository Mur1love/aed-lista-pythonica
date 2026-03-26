def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    """
    Substitui um convidado indisponível por outro.

    Args:
        guests (list[str]): lista original
        unavailable (str): convidado a ser removido
        new_guest (str): novo convidado

    Returns:
        list[str]: lista atualizada
    """
    updated_guests = guests.copy()
    if unavailable in updated_guests:
        index = updated_guests.index(unavailable)
        updated_guests[index] = new_guest
    return updated_guests
