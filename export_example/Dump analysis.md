The export is a standard Telegram Desktop HTML export. Each file follows a rigid structure:

- `page_wrap > page_header + page_body.chat_page > history`

- Regular messages: `div.message.default.clearfix#messageNNNNNN` with sub-divs `.userpic_wrap`, `.from_name`, `.reply_to`, `.text`

- **Critical edge case**: `div.message.default.clearfix.joined` - consecutive messages by the same author omit both `.userpic_wrap` and `.from_name` entirely from the DOM

- Service messages (date banners): `div.message.service`

- Cross-page links: `<a href="#go_to_messageNNNNN" onclick="return GoToMessage(NNNNN)">` - these break when the target message is in a different file

- Pagination: `<a class="pagination block_link" href="messages2.html">` sits **inside** `.history` and must be filtered out during extraction

- Rich media types encoded via CSS classes: `media_photo`, `media_voice_message`, `media_video`, `media_audio_file`, `media_file`, `media_contact`, `media_location`, `media_venue`, `media_game`, `media_invoice`

- Reactions, spoilers, bot buttons all have dedicated CSS structures

- Full dark mode via `@media (prefers-color-scheme: dark)`

- `body onload="CheckLocation();"` handles `#go_to_messageNNNNN` hash on load

Scale arithmetic: 732 files is 493 MB of raw HTML. Each file is one page of messages; file naming follows `messages.html`, `messages2.html`, ..., `messages732.html`