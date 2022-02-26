require 'rails_helper'

describe 'Update status' do
  before do
    create_service
    login_super_admin
    visit '/admin/locations/vrs-services'
  end

  it 'with valid status' do
    click_link 'Literacy Program'
    select 'Defunct', from: 'service_status'
    click_button I18n.t('admin.buttons.save_changes')
    expect(page).to have_content 'Service was successfully updated.'
    expect(find_field('service_status').value).to eq 'defunct'
  end
end
