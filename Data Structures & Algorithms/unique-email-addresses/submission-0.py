class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_addresses = set()

        for email in emails:
            # 0: local name, 1: domain name
            name_parts = email.split("@")

            local_name = ''
            for ch in name_parts[0]:
                if ch == '.':
                    continue
                elif ch == '+':
                    break
                else:
                    local_name += ch

            unique_email_addresses.add(local_name + name_parts[1])

        return len(unique_email_addresses)