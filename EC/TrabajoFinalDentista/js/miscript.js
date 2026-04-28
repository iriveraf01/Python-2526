// Script for Dentify Application

// Client Modal Logic
function openHistoryModal() {
    const modal = document.getElementById('historyModal');
    if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    }
}

function closeHistoryModal() {
    const modal = document.getElementById('historyModal');
    if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    }
}

// Additional interactivity could be added here
