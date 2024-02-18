/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../..";
import * as core from "../../../../core";

export type Error =
    | SeedTrace.playlist.updatePlaylist.Error.PlaylistIdNotFoundError
    | SeedTrace.playlist.updatePlaylist.Error._Unknown;

export declare namespace Error {
    interface PlaylistIdNotFoundError extends _Utils {
        errorName: "PlaylistIdNotFoundError";
        content: SeedTrace.PlaylistIdNotFoundErrorBody;
    }

    interface _Unknown extends _Utils {
        errorName: void;
        content: core.Fetcher.Error;
    }

    interface _Utils {
        _visit: <_Result>(visitor: SeedTrace.playlist.updatePlaylist.Error._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        playlistIdNotFoundError: (value: SeedTrace.PlaylistIdNotFoundErrorBody) => _Result;
        _other: (value: core.Fetcher.Error) => _Result;
    }
}

export const Error = {
    playlistIdNotFoundError: (
        value: SeedTrace.PlaylistIdNotFoundErrorBody
    ): SeedTrace.playlist.updatePlaylist.Error.PlaylistIdNotFoundError => {
        return {
            content: value,
            errorName: "PlaylistIdNotFoundError",
            _visit: function <_Result>(
                this: SeedTrace.playlist.updatePlaylist.Error.PlaylistIdNotFoundError,
                visitor: SeedTrace.playlist.updatePlaylist.Error._Visitor<_Result>
            ) {
                return SeedTrace.playlist.updatePlaylist.Error._visit(this, visitor);
            },
        };
    },

    _unknown: (fetcherError: core.Fetcher.Error): SeedTrace.playlist.updatePlaylist.Error._Unknown => {
        return {
            errorName: undefined,
            content: fetcherError,
            _visit: function <_Result>(
                this: SeedTrace.playlist.updatePlaylist.Error._Unknown,
                visitor: SeedTrace.playlist.updatePlaylist.Error._Visitor<_Result>
            ) {
                return SeedTrace.playlist.updatePlaylist.Error._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(
        value: SeedTrace.playlist.updatePlaylist.Error,
        visitor: SeedTrace.playlist.updatePlaylist.Error._Visitor<_Result>
    ): _Result => {
        switch (value.errorName) {
            case "PlaylistIdNotFoundError":
                return visitor.playlistIdNotFoundError(value.content);
            default:
                return visitor._other(value as any);
        }
    },
} as const;